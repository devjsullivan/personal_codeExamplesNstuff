package com.company;

import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.HashMap;



public class Main {

    public static String dec2oct(Integer dec) {
        String octStr = new String();
        Integer left = 0;
        Integer step = 8*8;
        Integer flrInt;
        // Start with 8^2
        left = dec % step;
        flrInt = (int)(Math.floor(dec/step));
        octStr = "o" + octStr + flrInt.toString();
        while (left > 0)
        {
            step = step/8;
            dec=left;
            left=left % step;
            flrInt = (int)(Math.floor(dec/step));
            octStr = octStr + flrInt.toString();
        }
        return octStr;
    }

    public static void main(String[] args) {
        List<String> strings = Arrays.asList("abc", "", "bc", "efg", "abcd","", "jkl");
        List<String> filtered = strings.stream().filter(string -> !string.isEmpty()).collect(Collectors.toList());
        filtered.stream().forEach(System.out::println);
        strings.stream().forEach(System.out::println);

        //Random random = new Random();
        List<Integer> iL =  Arrays.asList(1, 100, 200, 300, 800);
        //forEach(System.out::println);
        System.out.println("Hi " + iL.get(1));
        //List<Integer> oL = iL.stream().forEach(System.out::println);


        List<Integer> numbers = Arrays.asList(3, 2, 2, 3, 7, 3, 5);

//get list of unique squares
        List<Integer> squaresList = numbers.stream().map( i -> i*i).distinct().collect(Collectors.toList());
        numbers.stream().forEach(System.out::println);
        squaresList.stream().forEach(System.out::println);


        List<String>str = Arrays.asList("abc", "", "bc", "efg", "abcd","", "jkl", "");

//get count of empty string
        long count = str.stream().filter(string -> string.isEmpty()).count();
        System.out.println("count " + count);
        System.out.println("Oct1 " + dec2oct(100));


        //HashMap<Integer, String> mOd  = iL.stream().collect(Collectors.toMap(i -> i.getKey(),  i -> "Hello"));
        //HashMap<Integer, String> mOd  = iL.stream().collect(Collectors.toMap(i,  i -> dec2oct(i));
        //mOd.entrySet().stream().forEach(System.out::println);
        HashMap<Integer, String> result = iL.stream().collect(Collectors.toMap(i -> i, i -> dec2oct(i)));
        result.entrySet().stream().forEach(System.out::println);
    }
}
