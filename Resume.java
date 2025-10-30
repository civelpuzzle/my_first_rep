package pz10;

public class Resume {
    private final String fullName;
    private final String email;
    private final String phone;

    private final String[] skills;
    private final String[] experiences;
    private final String[] education;

    private Resume(ResumeBuilder builder) {
        this.fullName = builder.fullName;
        this.email = builder.email;
        this.phone = builder.phone;
        this.skills = builder.skills.clone();
        this.experiences = builder.experiences.clone();
        this.education = builder.education.clone();
    }

    public String getFullName() {
        return fullName;
    }

    public String getEmail() {
        return email;
    }

    public String getPhone() {
        return phone;
    }

    public String[] getSkills() {
        return skills.clone();
    }

    public String[] getExperiences() {
        return experiences.clone();
    }

    public String[] getEducation() {
        return education.clone();
    }

    @Override
    public String toString() {
        return "Резюме: \n" +
                "ФИО: " + fullName + "\n" +
                "Email: " + email + "\n" +
                "Номер телефона: " + phone + "\n" +
                "Навыки: " + String.join(", ", skills) + "\n" +
                "Опыт работы: " + String.join("; ", experiences) + "\n" +
                "Образование: " + String.join("; ", education) + "\n";
    }

    public static class ResumeBuilder {
        private String fullName;
        private String email;
        private String phone;
        private String[] skills = new String[0];
        private String[] experiences = new String[0];
        private String[] education = new String[0];

        public ResumeBuilder setPersonalData(String fullName, String email, String phone) {
            this.fullName = fullName;
            this.email = email;
            this.phone = phone;
            return this;
        }

        public ResumeBuilder setSkills(String... skills) {
            this.skills = skills.clone();
            return this;
        }

        public ResumeBuilder setExperiences(String... experiences) {
            this.experiences = experiences.clone();
            return this;
        }

        public ResumeBuilder setEducation(String... education) {
            this.education = education.clone();
            return this;
        }

        public Resume build() {
            return new Resume(this);
        }
    }
}
