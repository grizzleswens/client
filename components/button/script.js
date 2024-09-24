/* In components/button/script.js */
(function () {
    if (document.querySelector(".button-component")) {
      document.querySelector(".button-component").onclick = function () {
        alert("Button clicked!");
      };
    }
  })();
  