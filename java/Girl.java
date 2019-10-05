class Girl extends Human {
    private String gender = "female";

    public static void main(String[] args) {
        Human me = new Human();
        System.out.println("This " + me.getType() + " is from " + me.getPlanet());
    }

    public String getGender() {
        return gender;
    }
}