package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class Base32Test {

    @Before
    public void setUp() throws Exception {
    }

    @After
    public void tearDown() throws Exception {
    }
//------------------------------ 1 ------------------------------

    @Test
    public void encodeBase32_FF() throws Exception {
        String encode = Base32.encodeBase32(-75314, -6);
        assertEquals("-29jk", encode);
    }

    @Test
    public void encodeBase32_FT() throws Exception {
        String encode = Base32.encodeBase32(-89563, 1);
        assertEquals("-2rfv", encode);
    }

    @Test
    public void encodeBase32_TF() throws Exception {
        String encode = Base32.encodeBase32(66666, -8);
        assertEquals("213b", encode);
    }

    @Test
    public void encodeBase32_TT() throws Exception {
        String encode = Base32.encodeBase32(88888, 7);
        assertEquals("0002qts", encode);
    }

    @Test
    public void encodeBase32_biggerM32() throws Exception {
        String encode = Base32.encodeBase32(-30, 7);
        assertEquals("-000000y", encode);
    }

//---------------------------------------------------------------


//------------------------------ 2 ------------------------------

    @Test
    public void decodeBase32_isNotNegative() throws Exception {
        long decode = Base32.decodeBase32("29jw");
        assertEquals(75324, decode);
    }

    @Test
    public void decodeBase32_isNegative() throws Exception {
        long decode = Base32.decodeBase32("-29jk");
        assertEquals(-75314, decode);
    }

    @Test
    public void decodeBase32_hash_w() throws Exception {
        long decode = Base32.decodeBase32("w");
        assertEquals(28, decode);
    }

    @Test
    public void decodeBase32_hash_j() throws Exception {
        long decode = Base32.decodeBase32("-j");
        assertEquals(-17, decode);
    }

//---------------------------------------------------------------


//------------------------------ 3 ------------------------------

    @Test
    public void getCharIndexIsBase32Character() throws Exception{
        Integer result = Base32.getCharIndex('b');
        long intgerToLong = result;
        assertEquals(10, intgerToLong);
    }

    @Test(expected = Exception.class)
    public void getCharIndexIsNotBase32Character() throws Exception{
        Integer result = Base32.getCharIndex('a');

    }

//---------------------------------------------------------------

//------------------------------ 4 ------------------------------

    @Test
    public  void encodeBase32_F() throws Exception {
        String encode = Base32.encodeBase32(-6666);
        assertEquals("-0000000006hb", encode);

    }


    @Test
    public  void encodeBase32_T() throws Exception {
        String encode = Base32.encodeBase32(75324);
        assertEquals("0000000029jw", encode);

    }

//---------------------------------------------------------------

}