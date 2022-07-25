let done = document.querySelector(".todo-done");
console.log(done);
console.log(done.parentElement.parentElement);
done.addEventListener("click", (e) => {
  e.target.parentElement.parentElement.style.backgroundColor = "green";
  e.target.parentElement.parentElement.style.opacity = "50%";
});
