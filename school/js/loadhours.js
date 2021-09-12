$(function() {

    console.log("hello loadhour");

    var groups = localStorage.getItem("groups");
    console.log(groups);

    console.log(JSON.parse(groups));
});