package com.frankyy;

import java.io.*;
import java.util.ArrayList;
import java.util.Collections;

public class Main {

    static String readline(String filename, int linen) throws IOException {
        BufferedReader r1= new BufferedReader(new InputStreamReader(
                new FileInputStream(filename)));
        String line =r1.readLine();
        if(linen<0 || linen > getlines(filename)){
            System.out.print("行数超出范围\n"+linen);
        }
        int num = 0;
        String back=new String("1");
        while(line != null){
            if(linen == ++num){
                //System.out.println("存入的值为："+line+"\n"+"该值在文本第【"+linen+"】行\n");
                back=line;
            }
            line=r1.readLine();
        }
        r1.close();
        return back;

    }
    static int getlines(String filename)throws IOException{
        BufferedReader in = new BufferedReader(new InputStreamReader(
                new FileInputStream(filename)));
        LineNumberReader r = new LineNumberReader(in);
        String s =r.readLine();
        int lines =0;
        while(s!=null){
            lines++;
            s=r.readLine();

        }
        r.close();
        in.close();
        return lines;
    }
    static void write(ArrayList dc, ArrayList<Cun> cun1) {
        try {
            //读取精选小数据集

            String content = "item_id item_list\n";

            File file = new File("/Users/YAO/.spyder-py3/atest/精选小数据集输出改.txt");

            // if file doesnt exists, then create it
            if (!file.exists()) {
                file.createNewFile();
            }

            FileWriter fw = new FileWriter(file.getAbsoluteFile());
            BufferedWriter bw = new BufferedWriter(fw);
            bw.write(content);
            int i=0,j=0,c=0;
            for(i=0;i<dc.size();i++){
                for(j=0;j<cun1.size();j++){
                    if(dc.get(i).equals((cun1.get(j)).ID)){
                        //for(int w4=1; w4<cun1.size(); w4++) {
                        int w4=j;
                        bw.write(cun1.get(w4).ID+" ");
                        bw.write(cun1.get(w4).fc.get(0)+"");
                        for(int w5=1; w5<cun1.get(w4).fc.size(); w5++){
                            bw.write(","+cun1.get(w4).fc.get(w5));
                        }// System.out.println();
                        bw.write("\n");
                        c++;
                        break;
                    }
                }
            }
            System.out.println("cun1判断的数量"+c);
            System.out.println("写入完成，cun1.size="+cun1.size());
            bw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) throws IOException {
        String filename = "/Users/YAO/.spyder-py3/atest/待预测商品列表test_items（new).txt";//del 小
        int alines = getlines(filename);
        int linen =2;
        ArrayList dc = new ArrayList();//dc=待测ID
        while(linen <= alines) {
            String ss= readline(filename, linen++);
            dc.add(ss);
            if((linen>=1000) && (linen%1000==0)) System.out.println("待预测数据读取到第["+linen+"]行");
        }

        //repeat
        filename = "/Users/YAO/.spyder-py3/atest/商品信息dim_items（new).txt";//
        //文件总行数
        alines = getlines(filename);

        //System.out.println("总行数有" + alines + "行\n");

        //指定行号码
        linen = 2;

        ArrayList<D> list1 = new ArrayList();
        ArrayList<D> list2 = new ArrayList();
        ArrayList<Cun> cun1 = new ArrayList();
        int i=0;
        A:while(linen <= alines) {
            String[] ss= readline(filename, linen++).trim().split("\\s+");
            D d=new D();//一定要放在里面，否则读入的数都不会更新
            if(ss.length<3) continue A;
            d.ID=ss[0];
            d.lm=ss[1];
            //d.fc=(ArrayList)ss[2].split(",");
            Collections.addAll(d.fc, (ss[2].split(",")));
            ////////System.out.println("!!!!!!!!!!!"+list1.get(i).ID);
            for(i=0;i<dc.size();i++){
                if(d.ID.equals(dc.get(i))){
                    d.f=1;
                    //System.out.println("读到需要比较的数，在list1中第【"+i+"]ID="+d.ID);
                }}
            i=0;
            list1.add(d);
            if((linen>=1000) && (linen%1000==0)) {
                System.out.println("总数据读取到第[" + linen + "]行");
            }
        }
        i=0;
        int t=0,count=0,n=0,m=0,tt=0;//i为需要比较的那一行
        //记录每一条待测ID分词与其他行数据相同的个数
        while(i<list1.size()){
            if(list1.get(i).f==1) {
                //!System.out.println("找到标记ID="+list1.get(i).ID);
                tt++;
                for (t=0; t < list1.size(); t++) {
                    //比较分词相同的个数
                    list1.get(t).count=0;
                    for (n=0; n < list1.get(i).fc.size(); n++) {
                        for (m=0; m < list1.get(t).fc.size(); m++) {
                            if ((list1.get(i).fc.get(n)).equals(list1.get(t).fc.get(m))) {
                                count++;
                            }
                        }}
                    list1.get(t).count = count;
                    count=0;
                }
                //!System.out.println("标记ID="+list1.get(i).ID+"的count="+list1.get(i).count);
                Cun cc=new Cun();
                cc.ID=list1.get(i).ID;
                list2.addAll(list1);
                //按照某列排序
                myc mc = new myc();
                Collections.sort(list2, mc);


                //write
                for(int w3=1;w3<=200;w3++) cc.fc.add(list2.get(w3).ID);
                cun1.add(cc);
                list2.clear();
                //System.out.println(list1.get(0).count);

            }
            i++;

        }
        System.out.println("共比较了"+tt+"个数字");

            /*for(int w4=1; w4<cun1.size(); w4++) {
                System.out.print("缓存中ID="+cun1.get(w4).ID+" ");
                for(int w5=0; w5<cun1.get(w4).fc.size(); w5++)
                    System.out.print(cun1.get(w4).fc.get(w5)+",");
                System.out.println();
            }*/

        System.out.println("！写入ID的数量:"+cun1.size());
        write(dc, cun1);
    }
    }

