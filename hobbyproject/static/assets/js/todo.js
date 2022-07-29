let startTime = document.querySelector(".start-time-input");
let endTime = document.querySelector(".end-time-input");
startTime.addEventListener("focusout", (e) => {
  endTime.setAttribute("min", startTime.value);
});

let todoInput = document.querySelector(".todo-input");
if (todoInput) {
  inputValue = todoInput.value;
  todoInput.focus();
  todoInput.value = " ";
  todoInput.value = inputValue;
}

let endTimes = document.querySelectorAll(".end-time");
var max = 0;
var list = [];
for (let et of endTimes) {
  let date = new Date(et.innerHTML);

  let diff = date - Date.now();
  if (diff > max) {
    max = diff;
  }
  list.push(date - Date.now());
}

for (let et of endTimes) {
  if (et.innerHTML == "") continue;
  let date = new Date(et.innerHTML);
  let diff = date - Date.now();
  et.parentElement.parentElement.style.backgroundColor =
    "rgba(20, 157, 221," + String(1 - diff / max) + ")";
  console.log(1 - diff / max);
}

// todo list에 있는 component들 중 완료된
let todoComponents = document.querySelectorAll(".todo-component");

for (let todo of todoComponents) {
  if (todo.classList.contains("done")) {
    todo.style.backgroundColor = "rgba(128,128,128,0.3)";
    todo.classList.add("text-decoration-line-through");
    todo.style.opacity = "50%";
  }
}
