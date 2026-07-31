(function () {
  "use strict";

  const STORAGE_PREFIX = "research-log-edits-v1:";
  const stateKey = STORAGE_PREFIX + location.pathname;
  // Capture the unrendered notebook while <x-dc> is still present. The runtime
  // replaces it at DOMContentLoaded, but the original structure is what we need
  // when baking browser edits back into a complete, reusable HTML file.
  const sourceDocument = document.documentElement.cloneNode(true);
  let state = loadState();
  let hydrating = false;

  function emptyState() {
    return { items: {}, extras: {} };
  }

  function loadState() {
    try {
      const stored = localStorage.getItem(stateKey);
      if (stored) return normalizeState(JSON.parse(stored));
    } catch (_) {}

    return emptyState();
  }

  function normalizeState(value) {
    const next = value && typeof value === "object" ? value : {};
    return {
      items: next.items && typeof next.items === "object" ? next.items : {},
      extras: next.extras && typeof next.extras === "object" ? next.extras : {},
    };
  }

  function saveState(message) {
    try {
      localStorage.setItem(stateKey, JSON.stringify(state));
      setStatus(message || "Saved locally");
    } catch (_) {
      setStatus("Browser autosave unavailable");
    }
  }

  function setStatus(message) {
    const status = document.querySelector("[data-editor-status]");
    if (!status) return;
    status.textContent = message;
    clearTimeout(setStatus.timer);
    setStatus.timer = setTimeout(() => {
      if (status.isConnected) status.textContent = "Click text to edit · saves in this browser";
    }, 1800);
  }

  function installStyles() {
    if (document.getElementById("research-log-editor-styles")) return;
    const style = document.createElement("style");
    style.id = "research-log-editor-styles";
    style.textContent = `
      .research-editor-toolbar {
        display:flex; align-items:center; gap:9px; flex-wrap:wrap;
        margin:-18px 0 28px; font-family:'IBM Plex Mono',monospace;
      }
      .research-editor-status { color:#8B8478; font-size:10px; margin-right:auto; }
      .research-editor-button, .research-editor-delete {
        appearance:none; border:1px solid #C4BCAB; background:#F4F1EA; color:#4A443B;
        cursor:pointer; font:500 10px/1 'IBM Plex Mono',monospace; letter-spacing:.04em;
      }
      .research-editor-button { border-radius:2px; padding:8px 10px; }
      .research-editor-button:hover, .research-editor-button:focus-visible {
        border-color:#8C2F1F; color:#8C2F1F; outline:none;
      }
      .research-editor-item { position:relative; padding-right:28px !important; }
      .research-editor-delete {
        position:absolute; right:2px; top:4px; width:22px; height:22px; border:0;
        border-radius:50%; color:#A39B8C; opacity:0; transition:opacity .15s;
      }
      .research-editor-item:hover > .research-editor-delete,
      .research-editor-item:focus-within > .research-editor-delete,
      .research-editor-delete:focus-visible { opacity:1; }
      .research-editor-delete:hover, .research-editor-delete:focus-visible {
        background:#EFE2DE; color:#8C2F1F; outline:none;
      }
      .research-editable {
        border-radius:2px; cursor:text; outline:none;
        text-decoration:underline dotted transparent;
        text-decoration-thickness:1px; text-underline-offset:4px;
      }
      .research-editable:hover { text-decoration-color:#C4BCAB; }
      .research-editable:focus {
        background:#FFF9F0; box-shadow:0 0 0 4px #FFF9F0;
        text-decoration-color:#8C2F1F;
      }
      .research-editor-assumption-label {
        color:#8C2F1F; flex:none; font:500 12px/1.6 'IBM Plex Mono',monospace;
      }
      .research-editor-extra-assumption {
        display:flex; gap:14px; align-items:flex-start; font-size:15px; line-height:1.6;
      }
      .research-editor-extra-next {
        display:flex; gap:12px; font-size:15px; line-height:1.6;
      }
      .research-editor-extra-next::before {
        content:'□'; color:#A39B8C; flex:none; font-family:'IBM Plex Mono',monospace;
      }
      @media print {
        .research-editor-toolbar, .research-editor-delete { display:none !important; }
        .research-editable { text-decoration:none !important; }
      }
    `;
    document.head.appendChild(style);
  }

  function installToolbar() {
    const tabs = document.querySelector(".entry-tabs");
    if (!tabs || document.querySelector(".research-editor-toolbar")) return;
    const toolbar = document.createElement("div");
    toolbar.className = "research-editor-toolbar";
    toolbar.innerHTML = `
      <span class="research-editor-status" data-editor-status>Click text to edit · saves in this browser</span>
      <button type="button" class="research-editor-button" data-editor-action="add">+ Add item</button>
      <button type="button" class="research-editor-button" data-editor-action="save">Save HTML</button>
      <button type="button" class="research-editor-button" data-editor-action="reset">Reset edits</button>
    `;
    tabs.insertAdjacentElement("afterend", toolbar);
  }

  function panelItems(panel) {
    const type = panel.dataset.panel;
    if (type === "work") {
      const directParagraphs = Array.from(panel.children).filter((node) => node.tagName === "P");
      const listItems = Array.from(panel.querySelectorAll("ul > li"));
      return directParagraphs.concat(listItems);
    }
    if (panel.tagName === "OL" || panel.tagName === "UL") {
      return Array.from(panel.children).filter((node) => node.tagName === "LI");
    }
    return Array.from(panel.querySelectorAll("ul > li"));
  }

  function textTarget(item, type) {
    if (type === "assumptions") {
      return item.querySelector("div > div") || item.querySelector("span:last-of-type");
    }
    const spans = Array.from(item.querySelectorAll(":scope > span")).filter(
      (span) => !span.classList.contains("astra-value"),
    );
    if (spans.length > 1) return spans[spans.length - 1];
    if (spans.length === 1 && item.childNodes.length > 1) return spans[0];
    return null;
  }

  function wrapItemText(item) {
    const editable = document.createElement("span");
    while (item.firstChild) editable.appendChild(item.firstChild);
    item.appendChild(editable);
    return editable;
  }

  function cleanHtml(value) {
    const template = document.createElement("template");
    template.innerHTML = value;
    template.content.querySelectorAll("script,style,iframe,object,embed,link,meta").forEach((node) => node.remove());
    template.content.querySelectorAll("*").forEach((node) => {
      for (const attribute of Array.from(node.attributes)) {
        if (attribute.name.toLowerCase().startsWith("on")) node.removeAttribute(attribute.name);
        if (
          (attribute.name === "href" || attribute.name === "src") &&
          /^\s*javascript:/i.test(attribute.value)
        ) {
          node.removeAttribute(attribute.name);
        }
      }
    });
    return template.innerHTML;
  }

  function prepareItem(item, key, type) {
    if (item.dataset.editorPrepared === key) return;
    item.dataset.editorPrepared = key;
    item.dataset.editorItemKey = key;
    item.classList.add("research-editor-item");

    let target = textTarget(item, type);
    if (!target) target = wrapItemText(item);
    target.classList.add("research-editable");
    target.dataset.editKey = key;
    target.setAttribute("contenteditable", "true");
    target.setAttribute("spellcheck", "true");
    target.setAttribute("role", "textbox");
    target.setAttribute("aria-multiline", "true");

    const saved = state.items[key];
    if (saved && typeof saved.content === "string") target.innerHTML = cleanHtml(saved.content);
    if (saved && saved.deleted) {
      item.hidden = true;
      item.style.setProperty("display", "none", "important");
    }

    const remove = document.createElement("button");
    remove.type = "button";
    remove.className = "research-editor-delete";
    remove.dataset.editorAction = "delete";
    remove.dataset.itemKey = key;
    remove.setAttribute("aria-label", "Delete this item");
    remove.title = "Delete this item";
    remove.textContent = "×";
    item.appendChild(remove);
  }

  function panelKey(panel) {
    const article = panel.closest("article");
    return `${article ? article.id : "entry"}:${panel.dataset.panel}`;
  }

  function renderExtras(panel) {
    const key = panelKey(panel);
    const extras = Array.isArray(state.extras[key]) ? state.extras[key] : [];
    const type = panel.dataset.panel;
    const container = type === "next" && panel.tagName !== "UL"
      ? panel.querySelector("ul") || panel
      : panel;

    for (const extra of extras) {
      if (!extra || !extra.id || container.querySelector(`[data-extra-id="${extra.id}"]`)) continue;
      const item = document.createElement(type === "work" ? "p" : "li");
      item.dataset.extraId = extra.id;

      if (type === "assumptions") {
        item.className = "research-editor-extra-assumption";
        const label = document.createElement("b");
        label.className = "research-editor-assumption-label";
        label.textContent = `A${panelItems(panel).length + 1}`;
        const text = document.createElement("span");
        text.textContent = extra.content || "New assumption";
        item.append(label, text);
      } else if (type === "next") {
        item.className = "research-editor-extra-next";
        const text = document.createElement("span");
        text.textContent = extra.content || "New next step";
        item.appendChild(text);
      } else {
        item.textContent = extra.content || "New work note";
      }
      container.appendChild(item);
      prepareItem(item, `${key}:extra:${extra.id}`, type);
    }
  }

  function hydrate() {
    if (hydrating) return;
    hydrating = true;
    try {
      installStyles();
      installToolbar();
      document.querySelectorAll("[data-panel]").forEach((panel) => {
        renderExtras(panel);
        panelItems(panel).forEach((item, index) => {
          if (item.dataset.extraId) return;
          const key = item.dataset.editorId || `${panelKey(panel)}:${index + 1}`;
          prepareItem(item, key, panel.dataset.panel);
        });
      });
    } finally {
      hydrating = false;
    }
  }

  function activePanel() {
    return Array.from(document.querySelectorAll("[data-panel]")).find((panel) => !panel.hidden);
  }

  function addItem() {
    const panel = activePanel();
    if (!panel) return;
    const key = panelKey(panel);
    if (!Array.isArray(state.extras[key])) state.extras[key] = [];
    const id = `${Date.now()}-${Math.random().toString(36).slice(2, 7)}`;
    const defaults = {
      work: "New work note",
      assumptions: "New assumption",
      next: "New next step",
    };
    state.extras[key].push({ id, content: defaults[panel.dataset.panel] });
    saveState("Item added");
    renderExtras(panel);
    const editable = panel.querySelector(`[data-extra-id="${id}"] .research-editable`);
    if (editable) {
      editable.focus();
      const selection = window.getSelection();
      const range = document.createRange();
      range.selectNodeContents(editable);
      selection.removeAllRanges();
      selection.addRange(range);
    }
  }

  function deleteItem(key) {
    if (!state.items[key]) state.items[key] = {};
    state.items[key].deleted = true;
    const item = document.querySelector(`[data-editor-item-key="${CSS.escape(key)}"]`);
    if (item) {
      item.hidden = true;
      item.style.setProperty("display", "none", "important");
    }
    saveState("Item deleted");
  }

  function sourcePanelItems(panel) {
    return panelItems(panel);
  }

  function appendSavedExtra(panel, extra, type, key) {
    const saved = state.items[key] || {};
    if (saved.deleted) return;
    const container = type === "next" && panel.tagName !== "UL"
      ? panel.querySelector("ul") || panel
      : panel;
    const item = document.createElement(type === "work" ? "p" : "li");
    item.dataset.extraId = extra.id;
    item.dataset.editorId = key;

    if (type === "assumptions") {
      item.className = "research-editor-extra-assumption";
      const label = document.createElement("b");
      label.className = "research-editor-assumption-label";
      label.textContent = `A${sourcePanelItems(panel).length + 1}`;
      const text = document.createElement("span");
      text.innerHTML = cleanHtml(saved.content || extra.content || "New assumption");
      item.append(label, text);
    } else if (type === "next") {
      item.className = "research-editor-extra-next";
      const text = document.createElement("span");
      text.innerHTML = cleanHtml(saved.content || extra.content || "New next step");
      item.appendChild(text);
    } else {
      item.innerHTML = cleanHtml(saved.content || extra.content || "New work note");
    }
    container.appendChild(item);
  }

  function buildSavedHtml() {
    const root = sourceDocument.cloneNode(true);
    root.querySelectorAll("[data-panel]").forEach((panel) => {
      const type = panel.dataset.panel;
      const keyBase = panelKey(panel);
      sourcePanelItems(panel).forEach((item, index) => {
        const key = item.dataset.editorId || `${keyBase}:${index + 1}`;
        const saved = state.items[key];
        if (saved && saved.deleted) {
          item.remove();
          return;
        }
        item.dataset.editorId = key;
        if (saved && typeof saved.content === "string") {
          let target = textTarget(item, type);
          if (!target) target = wrapItemText(item);
          target.innerHTML = cleanHtml(saved.content);
        }
      });

      const extras = Array.isArray(state.extras[keyBase]) ? state.extras[keyBase] : [];
      extras.forEach((extra) => {
        if (!extra || !extra.id) return;
        appendSavedExtra(panel, extra, type, `${keyBase}:extra:${extra.id}`);
      });
    });

    root.querySelectorAll(".research-editor-toolbar, .research-editor-delete").forEach((node) => node.remove());
    root.querySelectorAll(".research-editable, .research-editor-item").forEach((node) => {
      node.classList.remove("research-editable", "research-editor-item");
      node.removeAttribute("contenteditable");
      node.removeAttribute("spellcheck");
      node.removeAttribute("role");
      node.removeAttribute("aria-multiline");
      node.removeAttribute("data-edit-key");
      node.removeAttribute("data-editor-item-key");
      node.removeAttribute("data-editor-prepared");
    });
    return "<!DOCTYPE html>\n" + root.outerHTML;
  }

  async function saveHtml() {
    const html = buildSavedHtml();
    const fileName = decodeURIComponent(location.pathname.split("/").pop() || "research-log.html");

    try {
      if (window.showSaveFilePicker) {
        const handle = await window.showSaveFilePicker({
          suggestedName: fileName,
          types: [{ description: "HTML document", accept: { "text/html": [".html"] } }],
        });
        const writable = await handle.createWritable();
        await writable.write(html);
        await writable.close();
        setStatus("HTML saved");
        return;
      }
    } catch (error) {
      if (error && error.name === "AbortError") {
        setStatus("Save cancelled");
        return;
      }
    }

    const blob = new Blob([html], { type: "text/html;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.download = fileName;
    document.body.appendChild(link);
    link.click();
    link.remove();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
    setStatus("HTML downloaded");
  }

  function resetEdits() {
    if (!window.confirm("Reset all edits for this notebook?")) return;
    try {
      localStorage.removeItem(stateKey);
    } catch (_) {}
    state = emptyState();
    location.reload();
  }

  document.addEventListener("input", (event) => {
    const target = event.target.closest && event.target.closest(".research-editable");
    if (!target) return;
    const key = target.dataset.editKey;
    if (!state.items[key]) state.items[key] = {};
    state.items[key].content = cleanHtml(target.innerHTML);
    saveState();
  });

  document.addEventListener("paste", (event) => {
    const target = event.target.closest && event.target.closest(".research-editable");
    if (!target) return;
    event.preventDefault();
    document.execCommand("insertText", false, event.clipboardData.getData("text/plain"));
  });

  document.addEventListener("click", (event) => {
    const button = event.target.closest && event.target.closest("[data-editor-action]");
    if (!button) return;
    event.preventDefault();
    event.stopPropagation();
    const action = button.dataset.editorAction;
    if (action === "add") addItem();
    if (action === "delete") deleteItem(button.dataset.itemKey);
    if (action === "save") saveHtml();
    if (action === "reset") resetEdits();
  });

  const observer = new MutationObserver(hydrate);
  observer.observe(document.documentElement, { childList: true, subtree: true });
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", hydrate, { once: true });
  } else {
    hydrate();
  }
})();
