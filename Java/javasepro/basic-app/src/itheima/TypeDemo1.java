package itheima;

public class TypeDemo1 {
    public static void main(String[] args) {
        //理解自动类型转换
        byte a = 20;
        int b = a;//发生了自动类型转换
        System.out.println(a);
        System.out.println(b);

        int age = 23;
        double db = age;
        System.out.println(age);
        System.out.println(db);
    }
}
