const btn = document.querySelector("#back-to-top");
btn.addEventListener("click", () => {
  window.scrollTo(0, 0);
});

ScrollReveal({
  origin: "bottom",
  distance: "40px",
  duration: 700,
}).reveal(`
  #cultura,
  .imagem,
  #secundaria,
  #secundaria iframe,
  #cultivo,
  #cultivo h1,
  #cultivo p,
  .fotos,
  .lado-a-lado,
  #agua,
  #agua h1,
  #agua p,
  #calendario,
  #calendario h1,
  #calendario h2,
  #calendario p,
  .lua,
  #contatos,
  .zap,
  #integrantes,
  .unip`);

const header = document.querySelector("#page-header");
const headerClassList = header.classList;
const btnClassList = btn.classList;

window.addEventListener("scroll", () => {
  if (window.scrollY >= 80) {
    if (!headerClassList.contains("scrollHide")) {
      headerClassList.add("scrollHide");
    }
    btnClassList.remove("hide");
  } else {
    if (headerClassList.contains("scrollHide")) {
      headerClassList.remove("scrollHide");
    }
    btnClassList.add("hide");
  }
});
