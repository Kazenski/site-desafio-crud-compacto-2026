import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";

mermaid.initialize({
  startOnLoad: false,
  theme: "base",
  securityLevel: "loose",
  fontFamily: "Segoe UI, system-ui, sans-serif",
  themeVariables: {
    primaryColor: "#fff1e8",
    primaryBorderColor: "#e8590c",
    primaryTextColor: "#1f2430",
    lineColor: "#4b5366",
    secondaryColor: "#f6f7fb",
    tertiaryColor: "#ffffff",
    noteBkgColor: "#fff6e5",
    noteBorderColor: "#f59e0b",
    actorBkg: "#fff1e8",
    actorBorder: "#e8590c",
    signalColor: "#1f2430",
    labelBoxBkgColor: "#f0f2f8",
    fontSize: "14px",
  },
  // useMaxWidth:false = cada diagrama no tamanho natural; o container rola na horizontal se precisar
  flowchart: { curve: "basis", htmlLabels: true, padding: 12, useMaxWidth: false },
  sequence: { actorMargin: 40, messageMargin: 36, mirrorActors: false, wrap: true, width: 160, useMaxWidth: false },
  journey: { useMaxWidth: false },
  state: { useMaxWidth: false },
  class: { useMaxWidth: false },
});

await mermaid.run({ querySelector: ".mermaid" });

// ---------- lightbox (clique no diagrama para ampliar) ----------
const lightbox = document.getElementById("lightbox");

document.querySelectorAll(".diagram svg").forEach((svg) => {
  svg.addEventListener("click", () => {
    lightbox.innerHTML = "";
    const clone = svg.cloneNode(true);
    clone.removeAttribute("width");
    clone.removeAttribute("height");
    clone.style.maxWidth = "100%";
    clone.style.maxHeight = "100%";
    lightbox.appendChild(clone);
    lightbox.classList.add("open");
  });
});

lightbox.addEventListener("click", () => lightbox.classList.remove("open"));
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") lightbox.classList.remove("open");
});

// ---------- destaque do item ativo no menu lateral ----------
const links = [...document.querySelectorAll(".sidebar nav a[href^='#']")];
const sections = links
  .map((a) => document.querySelector(a.getAttribute("href")))
  .filter(Boolean);

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      links.forEach((a) => a.classList.remove("active"));
      const active = links.find((a) => a.getAttribute("href") === `#${entry.target.id}`);
      if (active) active.classList.add("active");
    });
  },
  { rootMargin: "-20% 0px -70% 0px" }
);

sections.forEach((s) => observer.observe(s));
