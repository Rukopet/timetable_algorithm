discipline = ["Математика", "Русский язык", "Литература", "Иностранный язык", "История", "Физическая культура", "Музыка", "Технология", "Химия", "Биология", "Физика", "Экология", "География", "Естествознание", "Астрономия", "Окружающий мир", "ИЗО", "Обществознание", "Информатика", "Геометрия"]
document.getElementById("discipline1").innerHTML = discipline[0];
document.getElementById("discipline2").innerHTML = discipline[1];
document.getElementById("discipline3").innerHTML = discipline[2];
document.getElementById("discipline4").innerHTML = discipline[3];
document.getElementById("discipline5").innerHTML = discipline[4];
document.getElementById("discipline6").innerHTML = discipline[5];
document.getElementById("discipline7").innerHTML = discipline[6];
document.getElementById("discipline8").innerHTML = discipline[7];
document.getElementById("discipline9").innerHTML = discipline[8];
document.getElementById("discipline10").innerHTML = discipline[9];
document.getElementById("discipline11").innerHTML = discipline[10];
document.getElementById("discipline12").innerHTML = discipline[11];
document.getElementById("discipline13").innerHTML = discipline[12];
document.getElementById("discipline14").innerHTML = discipline[13];
document.getElementById("discipline15").innerHTML = discipline[14];
document.getElementById("discipline16").innerHTML = discipline[15];
document.getElementById("discipline17").innerHTML = discipline[16];
document.getElementById("discipline18").innerHTML = discipline[17];
document.getElementById("discipline19").innerHTML = discipline[18];
document.getElementById("discipline20").innerHTML = discipline[19];

discipline.forEach((item) => {
    $('#pair').append('<option value="pair1">' + discipline[19] + '</option>');
    $('#pair').append('<option value="pair2">' + discipline[18] + '</option>');
});