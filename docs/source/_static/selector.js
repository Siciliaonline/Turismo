document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".doc-switcher__select").forEach(function (select) {
    select.addEventListener("change", function () {
      if (select.value && select.value !== "#") {
        window.location.href = select.value;
      }
    });
  });
});
