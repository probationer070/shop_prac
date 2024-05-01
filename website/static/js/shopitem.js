// let item_url = document.getElementsByClassName("item-url");
// let item_url2 = document.querySelector(".item-url");
// let item_url3 = document.getElementById("item-url");

// console.log("1", item_url.value);
// console.log("1", item_url);
// console.log("2", item_url2.value);
// console.log("2", item_url2);
// console.log("3", item_url3.value);
// console.log("3", item_url3);


let item_url = document.querySelector(".item-url");


item_url.addEventListener('click', () => {
  console.log(item_url.value);
  // const text = "http://127.0.0.1:5000" + item_url.value;
  location.href = item_url.value;
});