package pz10;

public class Program {
    public static void main(String[] args){
        Resume resume1 = new Resume.ResumeBuilder()
                .setPersonalData("Иванов Иван Иванович", "ivan@example.com", "+79990001122")
                .setSkills("Java", "OOP", "SQL")
                .setExperiences("Разработчик в компании Company A (2019-2021)", "Разработчик в компании Company B (2021-2025)")
                .setEducation("Университет Г, города Москва")
                .build();

        Resume resume2 = new Resume.ResumeBuilder()
                .setPersonalData("Петрова Анна Сергеевна", "anna@example.com", "+79991112233")
                .setSkills("Python", "Machine Learning", "Data Analysis")
                .setExperiences("Разработчик в компании Company C (2020-2021)")
                .setEducation("Колледж К, города Ростова-на-Дону")
                .build();

        System.out.println(resume1);
        System.out.println(resume2);
    }
}
