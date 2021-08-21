discipline = ["Математика", "Русский язык", "Литература", "Иностранный язык", "История", "Физическая культура", "Музыка", "Технология", "Химия", "Биология", "Физика", "Экология", "География", "Естествознание", "Астрономия", "Окружающий мир", "ИЗО", "Обществознание", "Информатика", "Геометрия"]

classnum = {
    "number": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    "letter": ["а", "б", "в", "г", "д"]
}

var groupsArray = []



$("#class1_par").change(function () {

    console.log("hello 1");
    if ($(this).val() == 'class1_par-1') {
        //выполняем код при выборе "Пункт 2"

        var groups = {
            "group1a": {
                "number": 1,
                "count": "a",
                "saturday_not_study": false
            }
        }

        console.log("hello 2");
        groupsArray.push(groups)

        console.log(groupsArray);

        var innergroup1 = $(".group1");
        innergroup1.append("<input type='checkbox' name='discipline1-pair' value='discipline1-pair'>");

        console.log("hello 3/1");

    } else {

        console.log("hello 3");
        // var filteredAry = groupsArray.filter(e => e !== 'group1')
        // var filteredgroups = groups.filter(function(e) { return e !== 'group1' })
        // console.log("deletItem");
        if ($(this).val() == 'class1_par-2') {
            var groups = {
                "group1a": {
                    "number": 1,
                    "count": "a",
                    "saturday_not_study": false
                },
                "group1b": {
                    "number": 1,
                    "count": "б",
                    "saturday_not_study": false
                }
            }
            groupsArray.push(groups)
            console.log(groupsArray);

            var innergroup2 = $(".group1");
            innergroup2.append("<input type='checkbox' name='class1-pair1' value='class1-pair1'> <input type='checkbox' name='class1-pair2' value='class1-pair2'>");
        } else {

            console.log("hello 5");
            // var filteredAry = groupsArray.filter(e => e !== 'group1')
            // var filteredgroups = groups.filter(function(e) { return e !== 'group1' })
            // console.log("deletItem");
            if ($(this).val() == 'class1_par-3') {
                var groups = {
                    "group1a": {
                        "number": 1,
                        "count": "a",
                        "saturday_not_study": false
                    },
                    "group1b": {
                        "number": 1,
                        "count": "б",
                        "saturday_not_study": false
                    },
                    "group1c": {
                        "number": 1,
                        "count": "в",
                        "saturday_not_study": false
                    }
                }
                groupsArray.push(groups)
                console.log(groupsArray);

                var innergroup3 = $(".group1");
                innergroup3.append("<input type='checkbox' name='class1-pair1' value='class1-pair1'> <input type='checkbox' name='class1-pair2' value='class1-pair2'> <input type='checkbox' name='class1-pair3' value='class1-pair3'>");

            } else {
                console.log("hello 6");
                // var filteredAry = groupsArray.filter(e => e !== 'group1')
                // var filteredgroups = groups.filter(function(e) { return e !== 'group1' })
                // console.log("deletItem");
                if ($(this).val() == 'class1_par-4') {
                    var groups = {
                        "group1a": {
                            "number": 1,
                            "count": "a",
                            "saturday_not_study": false
                        },
                        "group1b": {
                            "number": 1,
                            "count": "б",
                            "saturday_not_study": false
                        },
                        "group1c": {
                            "number": 1,
                            "count": "в",
                            "saturday_not_study": false
                        },
                        "group1d": {
                            "number": 1,
                            "count": "г",
                            "saturday_not_study": false
                        }
                    }
                    groupsArray.push(groups)
                    console.log(groupsArray);

                    var innergroup4 = $(".group1");
                    innergroup4.append("<input type='checkbox' name='class1-pair1' value='class1-pair1'> <input type='checkbox' name='class1-pair2' value='class1-pair2'> <input type='checkbox' name='class1-pair3' value='class1-pair3'> <input type='checkbox' name='class1-pair4' value='class1-pair4'>");

                } else {
                    console.log("hello 7");
                    // var filteredAry = groupsArray.filter(e => e !== 'group1')
                    // var filteredgroups = groups.filter(function(e) { return e !== 'group1' })
                    // console.log("deletItem");
                    if ($(this).val() == 'class1_par-5') {
                        var groups = {
                            "group1a": {
                                "number": 1,
                                "count": "a",
                                "saturday_not_study": false
                            },
                            "group1b": {
                                "number": 1,
                                "count": "б",
                                "saturday_not_study": false
                            },
                            "group1c": {
                                "number": 1,
                                "count": "в",
                                "saturday_not_study": false
                            },
                            "group1d": {
                                "number": 1,
                                "count": "г",
                                "saturday_not_study": false
                            },
                            "group1f": {
                                "number": 1,
                                "count": "д",
                                "saturday_not_study": false
                            }
                        }
                        groupsArray.push(groups)
                        console.log(groupsArray);

                        var innergroup = $(".group1");
                        innergroup.append("<input type='checkbox' name='class1-pair1' value='class1-pair1'> <input type='checkbox' name='class1-pair2' value='class1-pair2'> <input type='checkbox' name='class1-pair3' value='class1-pair3'> <input type='checkbox' name='class1-pair4' value='class1-pair4'> <input type='checkbox' name='class1-pair5' value='class1-pair5'>");
                    }
                }
            }
        }
    }
});
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