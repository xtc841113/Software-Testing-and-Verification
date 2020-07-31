package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;

public class GeoHashTest {
    private Set<String> hashes = new HashSet();
    private Set<String> hashes_1 = new HashSet();
    @Before
    public void setUp() throws Exception {
        hashes.add("29jq");
        hashes.add("29jy");
        hashes.add("29jx");
        hashes.add("29jt");
        hashes.add("29jr");
        hashes.add("29jm");
        hashes.add("29jz");
        hashes.add("29jv");

        hashes_1.add("29jw");
        hashes_1.add("29jy");
        hashes_1.add("29jx");
    }

    @After
    public void tearDown() throws Exception {
    }

//------------------------------ 5 ------------------------------

    @Test
    public void top_F() throws Exception{
        String result = GeoHash.top("-29xy");
        assertEquals("-2c8n",result);
    }

    @Test
    public void top_T() throws Exception{
        String result = GeoHash.top("29jw");
        assertEquals("29jx",result);
    }

//---------------------------------------------------------------


//------------------------------ 6 ------------------------------

    @Test
    public void bottom_F() throws Exception{
        String result = GeoHash.bottom("-30xx");
        assertEquals("-30xr",result);
    }

    @Test
    public void bottom_T() throws Exception{
        String result = GeoHash.bottom("88eq");
        assertEquals("88em",result);
    }

//---------------------------------------------------------------


//------------------------------ 7 ------------------------------

    @Test
    public void left_F() throws Exception{
        String result = GeoHash.left("-32ty");
        assertEquals("-32tv",result);
    }

    @Test
    public void left_T() throws Exception{
        String result = GeoHash.left("66py");
        assertEquals("66pw",result);
    }

//---------------------------------------------------------------


//------------------------------ 8 ------------------------------

    @Test
    public void right_F() throws Exception{
        String result = GeoHash.right("-00er");
        assertEquals("-00g2",result);
    }

    @Test
    public void right_T() throws Exception{
        String result = GeoHash.right("68jk");
        assertEquals("68js",result);
    }

//---------------------------------------------------------------


    @Test
    public void neighbours() throws Exception{
        List<String> list = new ArrayList<String>();

        list.add("29jq");
        list.add("29jy");
        list.add("29jx");
        list.add("29jt");
        list.add("29jr");
        list.add("29jm");
        list.add("29jz");
        list.add("29jv");

        assertThat(GeoHash.neighbours("29jw"), is(list));
    }



    @Test
    public void adjacentHash() throws Exception{
        String h = GeoHash.adjacentHash("29jw", Direction.LEFT, 3);
        assertEquals("29hy", h);
    }



    @Test
    public void adjacentHashStepsIsNegative() throws Exception{
        String h = GeoHash.adjacentHash("29jw", Direction.LEFT, -3);
        assertEquals("29nq", h);
    }

//------------------------------ 9 ------------------------------

    @Test
    public void hashLengthToCoverBoundingBox() throws Exception{
        int result = GeoHash.hashLengthToCoverBoundingBox(25.0289061,121.4889208,25.0361156,121.4639264);
        assertEquals(4,result);
    }

    @Test
    public void hashLengthToCoverBoundingBox_1() throws Exception{
        int result = GeoHash.hashLengthToCoverBoundingBox(25.0361156,121.4639264,25.0289061,121.4889208);
        assertEquals(4,result);
    }

    @Test
    public void hashLengthToCoverBoundingBox_2() throws Exception{
        int result = GeoHash.hashLengthToCoverBoundingBox(0,0,0,0);
        assertEquals(12,result);
    }

    @Test
    public void hashLengthToCoverBoundingBox_3() throws Exception{
        int result = GeoHash.hashLengthToCoverBoundingBox(0,45,45,0);
        assertEquals(0,result);
    }

    @Test
    public void hashLengthToCoverBoundingBox_4() throws Exception{
        int result = GeoHash.hashLengthToCoverBoundingBox(45,0,0,0);
        assertEquals(0,result);
    }

//---------------------------------------------------------------


//------------------------------ 10 ------------------------------

    @Test
    public void heightDegreesLessThan12() throws Exception{
        double result = GeoHash.heightDegrees(2);
        assertEquals(5.625, result,0.001);
    }

    @Test
    public void heightDegreesGreaterThan12() throws Exception{
        double result = GeoHash.heightDegrees(14);
        assertEquals(5.238689482212067E-9, result,0.001);
    }

//---------------------------------------------------------------


//------------------------------ 11 ------------------------------

    @Test(expected = Exception.class)
    public void adjacentHash_NULL() throws Exception{
        String h = GeoHash.adjacentHash(null, Direction.LEFT);
    }

    @Test
    public void adjacentHash_() throws Exception{
        String h = GeoHash.adjacentHash("19jw", Direction.LEFT);
        assertEquals("19jq",h);
    }


//---------------------------------------------------------------


//------------------------------ 12 ------------------------------

    @Test
    public void decodeHash() throws Exception{
        LatLong result = GeoHash.decodeHash("29jw");
        LatLong ll = new LatLong(-38.232421875, -149.58984375);
        assertEquals(ll.getLat(), result.getLat(),0.001);
        assertEquals(ll.getLon(), result.getLon(),0.001);
    }

    @Test(expected = Exception.class)
    public void decodeHash_() throws Exception{
        LatLong result = GeoHash.decodeHash(null);
        LatLong ll = new LatLong(-38.232421875, -149.58984375);
    }

//---------------------------------------------------------------


//------------------------------ 13 ------------------------------

    @Test
    public void encodeHash_T() throws Exception{
        LatLong ll = new LatLong(-38.232421875, -149.58984375);
        String result = GeoHash.encodeHash(ll,6);
        assertEquals("29jws0", result);
    }

    @Test(expected = Exception.class)//exception: length must be greater than zero
    public void encodeHash_F() throws Exception{
        LatLong ll = new LatLong(-38.232421875, -149.58984375);
        String result = GeoHash.encodeHash(ll,0);
    }

//---------------------------------------------------------------

    @Test
    public void encodeHashm_T() throws Exception{
        LatLong ll = new LatLong(-38.232421875, -149.58984375);
        String result = GeoHash.encodeHash(ll);
        assertEquals("29jws0000000", result);
    }

    @Test(expected = Exception.class)
    public void encodeHashLengthGreaterThan12() throws Exception{
        String result = GeoHash.encodeHash(-38.232421875, -149.58984375,15);
    }

    @Test(expected = Exception.class)
    public void encodeHashLengthEqual1() throws Exception{
        String result = GeoHash.encodeHash(-120.232421875, -149.58984375,1);
    }


//------------------------------ 14 ------------------------------

    @Test
    public void coverBoundingBox_F() throws Exception{
        Boolean result = GeoHash.hashContains("29jw",-38.232421875, -149.58984375);
        assertEquals(true, result);
    }

    @Test
    public void coverBoundingBox_T() throws Exception{
        Boolean result = GeoHash.hashContains("29jw",0, 0);
        assertEquals(false, result);
    }

//---------------------------------------------------------------

//------------------------------ 15 ------------------------------
    @Test
    public void widthDegrees_F() throws Exception{
        double n = GeoHash.widthDegrees(13);
        assertEquals(4.190951585769653E-8,n,0.001);
    }

    @Test
    public void widthDegrees_T() throws Exception{
        double n = GeoHash.widthDegrees(6);
        assertEquals(0.010986328125,n,0.001);
    }

    @Test
    public void coverBoundingBoxMaxHashes_1(){
        Coverage coverage = GeoHash.coverBoundingBoxMaxHashes(25.0361156,121.4639264,25.0289061,121.4889208, 4);
        assertEquals("Coverage [hashes=[wsqq7, wsqqk], ratio=21.434198480498]",coverage.toString());
    }

    @Test
    public void coverBoundingBoxMaxHashes_2(){
        Coverage coverage = GeoHash.coverBoundingBoxMaxHashes(25.0361156,121.4639264,25.0361156,121.4639264, 2);
        assertEquals("Coverage [hashes=[wsqq7vxmfw5y], ratio=Infinity]", coverage.toString());
    }

    @Test
    public void coverBoundingBoxMaxHashes_3(){
        Coverage coverage = GeoHash.coverBoundingBoxMaxHashes(25.0361156,
                                                              -121.4639264,
                                                              -25.0361156,
                                                              -121.4639264,
                                                               2);
        assertEquals("Coverage [hashes=[3, 9], ratio=Infinity]", coverage.toString());
    }

    @Test(expected = Exception.class)
    public void coverBoundingBoxMaxHashes_4(){
        Coverage coverage = GeoHash.coverBoundingBoxMaxHashes(1,-1,-1,-1, 1);
        assertEquals("", coverage.toString());
    }

    @Test(expected = Exception.class)
    public void coverBoundingBoxMaxHashes_5(){
        Coverage coverage = GeoHash.coverBoundingBoxMaxHashes(-1,-1,1,-1, 1);
        assertEquals("", coverage.toString());
    }

    @Test(expected = Exception.class)
    public void coverBoundingBoxMaxHashes_6(){
        Coverage coverage = GeoHash.coverBoundingBoxMaxHashes(-1,1,1,-1, 1);
        assertEquals("", coverage.toString());
    }

    @Test
    public void coverBoundingBox(){
        Coverage coverage = GeoHash.coverBoundingBox(25.0361156,121.4639264,25.0289061,121.4889208, 4);
        assertEquals("Coverage [hashes=[wsqq], ratio=342.947175687968]", coverage.toString());

    }

    @Test
    public void gridAsString_1(){ //不包含"29jw"
        String result = GeoHash.gridAsString("29jw",-1,-1,-1, 1,hashes);
        String expected = "29JR \n" + "29JQ \n" + "29JM \n";
        assertEquals(expected, result);
    }
    @Test
    public void gridAsString_2(){ //包含"29jw"
        String result = GeoHash.gridAsString("29jw",-1,-1,-1, 1,hashes_1);
        String expected = "29jr \n" + "29jq \n" + "29jm \n";
        assertEquals(expected, result);
    }

    @Test
    public void gridAsString_3(){ //包含"29jw"
        String result = GeoHash.gridAsString("29jw",-1,3,-1, 1,hashes_1);
        assertEquals("", result);
    }

    @Test
    public void gridAsString_4(){ //包含"29jw"
        String result = GeoHash.gridAsString("29jw",1,3,-1, 1,hashes_1);
        assertEquals("", result);
    }

    @Test
    public void gridAsString_5(){
        String result = GeoHash.gridAsString("29jw",3,hashes_1);
        assertEquals("29kc 29m1 29m3 29m9 29mc 29q1 29q3 \n" +
                "29kb 29m0 29m2 29m8 29mb 29q0 29q2 \n" +
                "29hz 29jp 29jr 29JX 29jz 29np 29nr \n" +
                "29hy 29jn 29jq 29JW 29JY 29nn 29nq \n" +
                "29hv 29jj 29jm 29jt 29jv 29nj 29nm \n" +
                "29hu 29jh 29jk 29js 29ju 29nh 29nk \n" +
                "29hg 29j5 29j7 29je 29jg 29n5 29n7 \n", result);
    }

    @Test
    public void gridAsString_6(){ //包含"29jw"
        String result = GeoHash.gridAsString("29jw",1,3,-1, 1);
        assertEquals("", result);
    }
}