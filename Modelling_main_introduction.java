//This is an introduction codes of ideas of modelling
//Please refer to the modelling file for more details
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
            System.out.print("Lines out of boundary!\n"+linen);
        }
        int num = 0;
        String back=new String("1");
        while(line != null){
            if(linen == ++num){
                
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

            String content = "item_id item_list\n";

            File file = new File("/Users/YAO/.spyder-py3/atest/selected_small_dataset.txt");

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
            System.out.println("cun1_number"+c);
            System.out.println("write compeleted，cun1.size="+cun1.size());
            bw.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) throws IOException {
	// write your code here
        String filename = "/Users/YAO/.spyder-py3/atest/predects_list_test_items（new).txt";//del 小
        int alines = getlines(filename);
        int linen =2;
        ArrayList dc = new ArrayList();//dc=待测ID
        while(linen <= alines) {
            String ss= readline(filename, linen++);
            dc.add(ss);
            if((linen>=1000) && (linen%1000==0)) System.out.println("Predects_list No.["+linen+"]");
        }

        //repeat
        filename = "/Users/YAO/.spyder-py3/atest/Dim_items（new).txt";//
        //No. of the files
        alines = getlines(filename);


        //manually choose a line number
        linen = 2;

        ArrayList<D> list1 = new ArrayList();
        ArrayList<D> list2 = new ArrayList();
        ArrayList<Cun> cun1 = new ArrayList();
        int i=0;
        A:while(linen <= alines) {
            String[] ss= readline(filename, linen++).trim().split("\\s+");
            D d=new D();
            if(ss.length<3) continue A;
            d.ID=ss[0];
            d.lm=ss[1];
            //d.fc=(ArrayList)ss[2].split(",");
            Collections.addAll(d.fc, (ss[2].split(",")));
            ////////System.out.println("!!!!!!!!!!!"+list1.get(i).ID);
            for(i=0;i<dc.size();i++){
                if(d.ID.equals(dc.get(i))){
                    d.f=1;
                   
                }}
            i=0;
            list1.add(d);
            if((linen>=1000) && (linen%1000==0)) {
                System.out.println("All_data Line No.[" + linen + "]");
            }
        }
        i=0;
        int t=0,count=0,n=0,m=0,tt=0;//i is the line to be compared
        //Record the number of ID tokens to be tested equal to other rows
        while(i<list1.size()){
            if(list1.get(i).f==1) {
                //!System.out.println("Found marked ID="+list1.get(i).ID);
                tt++;
                for (t=0; t < list1.size(); t++) {
                    //Compare the same number of participles
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
                //Sort by a column
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
        System.out.println("compared numbers are"+tt);
        System.out.println("Number of written IDs:"+cun1.size());
        write(dc, cun1);
    }
    }

