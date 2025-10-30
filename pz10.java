//package pz10;
//// Immutable Resume class with nested Builder class
//public class pz10 {
//    // Personal data fields
//    private final String fullName;
//    private final String email;
//    private final String phone;
//
//    // Skills, Experience, and Education can be lists
//    private final String[] skills;
//    private final String[] experiences;
//    private final String[] education;
//
//    private pz10(ResumeBuilder builder) {
//        this.fullName = builder.fullName;
//        this.email = builder.email;
//        this.phone = builder.phone;
//        this.skills = builder.skills.clone();
//        this.experiences = builder.experiences.clone();
//        this.education = builder.education.clone();
//    }
//
//    public String getFullName() {
//        return fullName;
//    }
//
//    public String getEmail() {
//        return email;
//    }
//
//    public String getPhone() {
//        return phone;
//    }
//
//    public String[] getSkills() {
//        return skills.clone();
//    }
//
//    public String[] getExperiences() {
//        return experiences.clone();
//    }
//
//    public String[] getEducation() {
//        return education.clone();
//    }
//
//    @Override
//    public String toString() {
//        StringBuilder sb = new StringBuilder();
//        sb.append("Resume: \n");
//        sb.append("Full Name: ").append(fullName).append("\n");
//        sb.append("Email: ").append(email).append("\n");
//        sb.append("Phone: ").append(phone).append("\n");
//        sb.append("Skills: ").append(String.join(", ", skills)).append("\n");
//        sb.append("Experience: ").append(String.join("; ", experiences)).append("\n");
//        sb.append("Education: ").append(String.join("; ", education)).append("\n");
//        return sb.toString();
//    }
//
//    public static class ResumeBuilder {
//        private String fullName;
//        private String email;
//        private String phone;
//        private String[] skills = new String[0];
//        private String[] experiences = new String[0];
//        private String[] education = new String[0];
//
//        public ResumeBuilder setPersonalData(String fullName, String email, String phone) {
//            this.fullName = fullName;
//            this.email = email;
//            this.phone = phone;
//            return this;
//        }
//
//        public ResumeBuilder setSkills(String... skills) {
//            this.skills = skills.clone();
//            return this;
//        }
//
//        public ResumeBuilder setExperiences(String... experiences) {
//            this.experiences = experiences.clone();
//            return this;
//        }
//
//        public ResumeBuilder setEducation(String... education) {
//            this.education = education.clone();
//            return this;
//        }
//
//        public pz10 build() {
//            return new pz10(this);
//        }
//    }
//}
//
//// Demo of usage
//class ResumeBuilderDemo {
//    public static void main(String[] args) {
//        pz10 resume1 = new pz10.ResumeBuilder()
//                .setPersonalData("Ivan Ivanov", "ivan@example.com", "+79990001122")
//                .setSkills("Java", "OOP", "SQL")
//                .setExperiences("Software developer at Company A (2019-2021)", "Senior developer at Company B (2021-present)")
//                .setEducation("Bachelor of Computer Science, University X")
//                .build();
//
//        pz10 resume2 = new pz10.ResumeBuilder()
//                .setPersonalData("Anna Petrova", "anna@example.com", "+79991112233")
//                .setSkills("Python", "Machine Learning", "Data Analysis")
//                .setExperiences("Data scientist at Company C (2020-present)")
//                .setEducation("Master in Data Science, University Y")
//                .build();
//
//        System.out.println(resume1);
//        System.out.println(resume2);
//    }
//}
