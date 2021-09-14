discipline = ["Математика", "Русский язык", "Литература", "Иностранный язык", "История", "Физическая культура", "Музыка", "Технология", "Химия", "Биология", "Физика", "Экология", "География", "Естествознание", "Астрономия", "Окружающий мир", "ИЗО", "Обществознание", "Информатика", "Геометрия"]

$(function() {
    
    console.log("hello subjects js");

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

    

    $("#subjects_next_page").click(function() {
        console.log('Кнопка нажата!');
        var subjects = getAllCurrent();
        localStorage.setItem("subjects", JSON.stringify(subjects));        
    })

});

function getAllCurrent() {

    var arr = [];
    $('.discipline_container').children('div').each(function () {
        console.log(this); // "this" is the current element in the loop

        var str = $( this).text().trim();
        arr.push(str);        
    });

    return arr;  
}