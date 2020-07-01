package com.frankyy;

import java.util.Comparator;

/**
 * Created by YAO on 2018/4/27.
 */
public class myc implements Comparator<D> {
    public int compare(D o1, D o2){
        if(o1.count>o2.count){
            return -1;}
        else if(o1.count==o2.count) return 0;
        else return 1;
    }
}
