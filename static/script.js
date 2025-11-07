document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("predictForm");
  form.addEventListener("submit", function () {
    setTimeout(() => {
      const result = document.querySelector(".result");
      if (result) {
        result.classList.add("fade-in");
      }
    }, 200);
  });
});
