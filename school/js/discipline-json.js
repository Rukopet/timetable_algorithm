discipline = ["Математика", "Русский язык", "Литература", "Иностранный язык", "История", "Физическая культура", "Музыка", "Технология", "Химия", "Биология", "Физика", "Экология", "География", "Естествознание", "Астрономия", "Окружающий мир", "ИЗО", "Обществознание", "Информатика", "Геометрия"]

// classnum = {
//     "number": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
//     "letter": ["а", "б", "в", "г", "д"]
// }

var groupsArray = []

let groups1 = [
    group1a = {
        "number": 1,
        "count": "а",
        "saturday_not_study": false
    },
    group1b = {
        "number": 1,
        "count": "б",
        "saturday_not_study": false
    },
    group1c = {
        "number": 1,
        "count": "в",
        "saturday_not_study": false
    },
    group1d = {
        "number": 1,
        "count": "г",
        "saturday_not_study": false
    },
    group1e = {
        "number": 1,
        "count": "д",
        "saturday_not_study": false
    },
    group1f = {
        "number": 1,
        "count": "е",
        "saturday_not_study": false
    }
]
let groups2 = [
    group2a = {
        "number": 2,
        "count": "а",
        "saturday_not_study": false
    },
    group2b = {
        "number": 2,
        "count": "б",
        "saturday_not_study": false
    },
    group2c = {
        "number": 2,
        "count": "в",
        "saturday_not_study": false
    },
    group2d = {
        "number": 2,
        "count": "г",
        "saturday_not_study": false
    },
    group2e = {
        "number": 2,
        "count": "д",
        "saturday_not_study": false
    },
    group2f = {
        "number": 2,
        "count": "е",
        "saturday_not_study": false
    }
]

$("#class1_par").change(function () {

    console.log("hello 1");

    if ($(this).val() == 'class1_par-1') {
        innergroup.removeChild
        for (i = 0; i < groupsArray.length; i++) {
            if (groupsArray[i] == group1a) {
                groupsArray.splice(i, 1);
            }
        }
        for (i = 0; i < groupsArray.length; i++) {
            if (groupsArray[i] == group1b) {
                groupsArray.splice(i, 1);
            }
        }
        for (i = 0; i < groupsArray.length; i++) {
            if (groupsArray[i] == group1c) {
                groupsArray.splice(i, 1);
            }
        }
        for (i = 0; i < groupsArray.length; i++) {
            if (groupsArray[i] == group1d) {
                groupsArray.splice(i, 1);
            }
        }
        for (i = 0; i < groupsArray.length; i++) {
            if (groupsArray[i] == group1e) {
                groupsArray.splice(i, 1);
            }
        }
        for (i = 0; i < groupsArray.length; i++) {
            if (groupsArray[i] == group1f) {
                groupsArray.splice(i, 1);
            }
        }

        groupsArray.push(group1a)

        console.log(groupsArray)

        let innergroup = $(".group1");
        innergroup.append("<input type='checkbox' name='group1a' value='group1a'>");
        console.log("hello 1/1");
    } else {
        if ($(this).val() == 'class1_par-2') {
            console.log("hello2")
            for (i = 0; i < groupsArray.length; i++) {
                if (groupsArray[i] == group1a) {
                    groupsArray.splice(i, 1);
                }
            }
            for (i = 0; i < groupsArray.length; i++) {
                if (groupsArray[i] == group1b) {
                    groupsArray.splice(i, 1);
                }
            }
            for (i = 0; i < groupsArray.length; i++) {
                if (groupsArray[i] == group1c) {
                    groupsArray.splice(i, 1);
                }
            }
            for (i = 0; i < groupsArray.length; i++) {
                if (groupsArray[i] == group1d) {
                    groupsArray.splice(i, 1);
                }
            }
            for (i = 0; i < groupsArray.length; i++) {
                if (groupsArray[i] == group1e) {
                    groupsArray.splice(i, 1);
                }
            }
            for (i = 0; i < groupsArray.length; i++) {
                if (groupsArray[i] == group1f) {
                    groupsArray.splice(i, 1);
                }
            }

            groupsArray.push(group1a, group1b)

            console.log(groupsArray);
            let innergroup = $(".group1");
            innergroup.append("<input type='checkbox' name='group1a' value='group1a'> <input type='checkbox' name='group1b' value='group1b'>");
            console.log("hello 2/1");
        }
        else {
            if ($(this).val() == 'class1_par-3') {
                console.log("hello3")
                for (i = 0; i < groupsArray.length; i++) {
                    if (groupsArray[i] == group1a) {
                        groupsArray.splice(i, 1);
                    }
                }
                for (i = 0; i < groupsArray.length; i++) {
                    if (groupsArray[i] == group1b) {
                        groupsArray.splice(i, 1);
                    }
                }
                for (i = 0; i < groupsArray.length; i++) {
                    if (groupsArray[i] == group1c) {
                        groupsArray.splice(i, 1);
                    }
                }
                for (i = 0; i < groupsArray.length; i++) {
                    if (groupsArray[i] == group1d) {
                        groupsArray.splice(i, 1);
                    }
                }
                for (i = 0; i < groupsArray.length; i++) {
                    if (groupsArray[i] == group1e) {
                        groupsArray.splice(i, 1);
                    }
                }
                for (i = 0; i < groupsArray.length; i++) {
                    if (groupsArray[i] == group1f) {
                        groupsArray.splice(i, 1);
                    }
                }

                groupsArray.push(group1a, group1b, group1c)

                console.log(groupsArray);
            }

            else {
                if ($(this).val() == 'class1_par-4') {
                    console.log("hello4")
                    for (i = 0; i < groupsArray.length; i++) {
                        if (groupsArray[i] == group1a) {
                            groupsArray.splice(i, 1);
                        }
                    }
                    for (i = 0; i < groupsArray.length; i++) {
                        if (groupsArray[i] == group1b) {
                            groupsArray.splice(i, 1);
                        }
                    }
                    for (i = 0; i < groupsArray.length; i++) {
                        if (groupsArray[i] == group1c) {
                            groupsArray.splice(i, 1);
                        }
                    }
                    for (i = 0; i < groupsArray.length; i++) {
                        if (groupsArray[i] == group1d) {
                            groupsArray.splice(i, 1);
                        }
                    }
                    for (i = 0; i < groupsArray.length; i++) {
                        if (groupsArray[i] == group1e) {
                            groupsArray.splice(i, 1);
                        }
                    }
                    for (i = 0; i < groupsArray.length; i++) {
                        if (groupsArray[i] == group1f) {
                            groupsArray.splice(i, 1);
                        }
                    }

                    groupsArray.push(group1a, group1b, group1c, group1d)

                    console.log(groupsArray);
                }
                else {
                    if ($(this).val() == 'class1_par-5') {
                        console.log("hello3")
                        for (i = 0; i < groupsArray.length; i++) {
                            if (groupsArray[i] == group1a) {
                                groupsArray.splice(i, 1);
                            }
                        }
                        for (i = 0; i < groupsArray.length; i++) {
                            if (groupsArray[i] == group1b) {
                                groupsArray.splice(i, 1);
                            }
                        }
                        for (i = 0; i < groupsArray.length; i++) {
                            if (groupsArray[i] == group1c) {
                                groupsArray.splice(i, 1);
                            }
                        }
                        for (i = 0; i < groupsArray.length; i++) {
                            if (groupsArray[i] == group1d) {
                                groupsArray.splice(i, 1);
                            }
                        }
                        for (i = 0; i < groupsArray.length; i++) {
                            if (groupsArray[i] == group1e) {
                                groupsArray.splice(i, 1);
                            }
                        }
                        for (i = 0; i < groupsArray.length; i++) {
                            if (groupsArray[i] == group1f) {
                                groupsArray.splice(i, 1);
                            }
                        }

                        groupsArray.push(group1a, group1b, group1c, group1d, group1e)

                        console.log(groupsArray);
                    }

                    else {
                        if ($(this).val() == 'class1_par-6') {
                            console.log("hello3")
                            for (i = 0; i < groupsArray.length; i++) {
                                if (groupsArray[i] == group1a) {
                                    groupsArray.splice(i, 1);
                                }
                            }
                            for (i = 0; i < groupsArray.length; i++) {
                                if (groupsArray[i] == group1b) {
                                    groupsArray.splice(i, 1);
                                }
                            }
                            for (i = 0; i < groupsArray.length; i++) {
                                if (groupsArray[i] == group1c) {
                                    groupsArray.splice(i, 1);
                                }
                            }
                            for (i = 0; i < groupsArray.length; i++) {
                                if (groupsArray[i] == group1d) {
                                    groupsArray.splice(i, 1);
                                }
                            }
                            for (i = 0; i < groupsArray.length; i++) {
                                if (groupsArray[i] == group1e) {
                                    groupsArray.splice(i, 1);
                                }
                            }
                            for (i = 0; i < groupsArray.length; i++) {
                                if (groupsArray[i] == group1f) {
                                    groupsArray.splice(i, 1);
                                }
                            }

                            groupsArray.push(group1a, group1b, group1c, group2d, group2e, group2f)

                            console.log(groupsArray);
                        }
                    }
                }
            }
        }

    }
});








// $("#class1_par").change(function () {

//     console.log("hello 1");
//     if ($(this).val() == 'class1_par-1') {
//         //выполняем код при выборе "Пункт 2"

//         var groups = {
//             "group1a": {
//                 "number": 1,
//                 "count": "a",
//                 "saturday_not_study": false
//             }
//         }

//         console.log("hello 2");
//         groupsArray.push(groups)

//         console.log(groupsArray);

//         var innergroup1 = $(".group1");
//         innergroup1.append("<input type='checkbox' name='discipline1-pair' value='discipline1-pair'>");
//         console.log("hello 3/1");

//     } else {

//         console.log("hello 3");
//         // console.log(groupsArray.indexOf(group1a));
//         // var index = groupsArray.indexOf(group1a);
//         // if(index > -1) groupsArray.splice(index, 1);
//         //  find the index in the array (-1 means not found):
//         // var index = groupsArray.indexOf(group1a, group1b, group1c, group1d, group1e);

//         //  remove the element at that index, if found:
//         // if(index > -1) groupsArray.splice(index, 1);
//         // var filteredAry = groupsArray.filter(e => e !== 'group1')
//         // var filteredgroups = groupsArray.filter(function(e) { return e !== 'groups' })
//         // console.log("deletItem");
//         if ($(this).val() == 'class1_par-2') {



//             var groups = {
//                 "group1a": {
//                     "number": 1,
//                     "count": "a",
//                     "saturday_not_study": false
//                 },
//                 "group1b": {
//                     "number": 1,
//                     "count": "б",
//                     "saturday_not_study": false
//                 }
//             }
//             groupsArray.push(groups)
//             console.log(groupsArray);

//             var innergroup = $(".group1");
//             innergroup.append("<input type='checkbox' name='class1-pair1' value='class1-pair1'> <input type='checkbox' name='class1-pair2' value='class1-pair2'>");
//         } else {

//             console.log("hello 5");
//             // var filteredAry = groupsArray.filter(e => e !== 'group1')
//             // var filteredgroups = groups.filter(function(e) { return e !== 'group1' })
//             // console.log("deletItem");
//             if ($(this).val() == 'class1_par-3') {
//                 var groups = {
//                     "group1a": {
//                         "number": 1,
//                         "count": "a",
//                         "saturday_not_study": false
//                     },
//                     "group1b": {
//                         "number": 1,
//                         "count": "б",
//                         "saturday_not_study": false
//                     },
//                     "group1c": {
//                         "number": 1,
//                         "count": "в",
//                         "saturday_not_study": false
//                     }
//                 }
//                 groupsArray.push(groups)
//                 console.log(groupsArray);

//                 var innergroup = $(".group1");
//                 innergroup.append("<input type='checkbox' name='class1-pair1' value='class1-pair1'> <input type='checkbox' name='class1-pair2' value='class1-pair2'> <input type='checkbox' name='class1-pair3' value='class1-pair3'>");

//             } else {
//                 console.log("hello 6");
//                 // var filteredAry = groupsArray.filter(e => e !== 'group1')
//                 // var filteredgroups = groups.filter(function(e) { return e !== 'group1' })
//                 // console.log("deletItem");
//                 if ($(this).val() == 'class1_par-4') {
//                     var groups = {
//                         "group1a": {
//                             "number": 1,
//                             "count": "a",
//                             "saturday_not_study": false
//                         },
//                         "group1b": {
//                             "number": 1,
//                             "count": "б",
//                             "saturday_not_study": false
//                         },
//                         "group1c": {
//                             "number": 1,
//                             "count": "в",
//                             "saturday_not_study": false
//                         },
//                         "group1d": {
//                             "number": 1,
//                             "count": "г",
//                             "saturday_not_study": false
//                         }
//                     }
//                     groupsArray.push(groups)
//                     console.log(groupsArray);

//                     var innergroup = $(".group1");
//                     innergroup.append("<input type='checkbox' name='class1-pair1' value='class1-pair1'> <input type='checkbox' name='class1-pair2' value='class1-pair2'> <input type='checkbox' name='class1-pair3' value='class1-pair3'> <input type='checkbox' name='class1-pair4' value='class1-pair4'>");

//                 } else {
//                     console.log("hello 7");
//                     // var filteredAry = groupsArray.filter(e => e !== 'group1')
//                     // var filteredgroups = groups.filter(function(e) { return e !== 'group1' })
//                     // console.log("deletItem");
//                     if ($(this).val() == 'class1_par-5') {
//                         var groups = {
//                             "group1a": {
//                                 "number": 1,
//                                 "count": "a",
//                                 "saturday_not_study": false
//                             },
//                             "group1b": {
//                                 "number": 1,
//                                 "count": "б",
//                                 "saturday_not_study": false
//                             },
//                             "group1c": {
//                                 "number": 1,
//                                 "count": "в",
//                                 "saturday_not_study": false
//                             },
//                             "group1d": {
//                                 "number": 1,
//                                 "count": "г",
//                                 "saturday_not_study": false
//                             },
//                             "group1e": {
//                                 "number": 1,
//                                 "count": "д",
//                                 "saturday_not_study": false
//                             }
//                         }
//                         groupsArray.push(groups)
//                         console.log(groupsArray);

//                         var innergroup = $(".group1");
//                         innergroup.append("<input type='checkbox' name='class1-pair1' value='class1-pair1'> <input type='checkbox' name='class1-pair2' value='class1-pair2'> <input type='checkbox' name='class1-pair3' value='class1-pair3'> <input type='checkbox' name='class1-pair4' value='class1-pair4'> <input type='checkbox' name='class1-pair5' value='class1-pair5'>");
//                     }
//                 }
//             }
//         }
//     }
// });


discipline.forEach((item, i, discipline) => {
    $('#pair').append('<option value="pair1">' + discipline[i] + '</option>');
});

var parent = $(".discipline_container");
for (let i = 0; i < discipline.length; i++) {
    const item = discipline[i];
    var id = "disp_one_cont" + i;
    parent.append("<div class='discipline' id='" + id + "' " +
        +"> <div class='discipline" + i + "' " + "id='discipline" + i + "' " + "> " + item + "  </div>   </div>");

    var innerParent = $("#" + id);
    innerParent.append("<div class='discipline-chek'> <input type='checkbox'  name='discipline" + i + "' " + " value='discipline" + i + "' " + " checked>     <input type='checkbox' name='discipline1-pair' value='discipline1-pair'> </div>");
}