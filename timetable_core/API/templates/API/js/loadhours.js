$(function() {

    console.log("hello loadhour");

    var groups = localStorage.getItem("groups");
    

    var subjects = localStorage.getItem("subjects");
     var  _subjects = JSON.parse(subjects);


    var _groups =  JSON.parse(groups);
    console.log(_groups);

    generateTable(_subjects, _groups);
});

// google - add table row foreach jquery
function generateTable(subjects, groups){
    
    addFirstRow(groups);
    var inputRow = getInputRow(groups);

    for (var i = 0; i < subjects.length; i++ ) {

        var subject = subjects[i];                    
        var tr_var ="<tr><td> " + subject + "</td>'" + inputRow + "</tr>";

        $(tr_var).appendTo('#tableSubjects');
    }
}

function addFirstRow(groups) {

    var head = "";
    for (let i = 0; i < groups.length; i++) {
        const group = groups[i];
        head += "<td> " + group.number + group.count + "</td>"
    }
    
    var p = "Предметы"
    console.log(head);
    var tr_var ="<tr><td> " + p + "</td>" + head + "</tr>";

    $(tr_var).appendTo('#tableSubjects');
}

function getInputRow(groups){
    var row = "";
    for (let i = 0; i < groups.length; i++) {     
        row += "<td> <input type='number'></td>"
    }
    return row;
}