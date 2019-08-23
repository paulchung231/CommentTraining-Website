function myFunction() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var json = JSON.parse(xhttp.responseText);
      document.getElementById("comment").innerHTML =
      json.comment_text;
      document.getElementById("feedback").innerHTML = ""
    }
  };
  xhttp.open("GET", "http://localhost:8000/randomComment/", true);
  xhttp.send();
}

function updateRating() {
  document.getElementById("feedback").innerHTML = "Changed rating!"
  // var xhttp = new XMLHttpRequest();
  // xhttp.onreadystatechange = function() {
  //   if (this.readyState == 4 && this.status == 200) {
  //     var json = JSON.parse(xhttp.responseText);
  //     document.getElementById("comment").innerHTML =
  //     json.comment_text;
  //   }
  // };
  // xhttp.open("GET", "http://localhost:8000/randomComment/", true);
  // xhttp.send();
}

// function myFunction() {
//     document.getElementById("comment").innerHTML = "Changed Check long sentence here to test the scrolling property." +
//         "Changed Check long sentence here to test the scrolling property. Changed Check long sentence here to test the scrolling property." +
//         "Changed Check long sentence here to test the scrolling property. Changed Check long sentence here to test the scrolling property." +
//         "Changed Check long sentence here to test the scrolling property. Changed Check long sentence here to test the scrolling property." +
//         "Changed Check long sentence here to test the scrolling property. Changed Check long sentence here to test the scrolling property." +
//         "Changed Check long sentence here to test the scrolling property. Changed Check long sentence here to test the scrolling property." +
//         "Changed Check long sentence here to test the scrolling property. Changed Check long sentence here to test the scrolling property." +
//         "Changed Check long sentence here to test the scrolling property. Changed Check long sentence here to test the scrolling property.";
// }
