package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.util.*;
import java.util.HashSet;

import static org.junit.Assert.*;

public class CoverageTest {

    private Coverage coverage;
    @Before
    public void setUp() throws Exception {
        Set<String> hashes = new HashSet();
        hashes.add("29jq");
        hashes.add("29jy");
        hashes.add("29jx");
        hashes.add("29jt");
        hashes.add("29jr");
        hashes.add("29jm");
        hashes.add("29jz");
        hashes.add("29jv");
        coverage = new Coverage(hashes, 6.6);
    }

    @After
    public void tearDown() throws Exception {
    }

    @Test
    public void getHash() throws Exception{
        Set<String> hashes = new HashSet();

        hashes.add("29jq");
        hashes.add("29jy");
        hashes.add("29jx");
        hashes.add("29jt");
        hashes.add("29jr");
        hashes.add("29jm");
        hashes.add("29jz");
        hashes.add("29jv");

        assertEquals(hashes, coverage.getHashes());
    }

    @Test
    public void getRatio() throws Exception{
        assertEquals(6.6, coverage.getRatio(),0.001);
    }

    @Test
    public void getHashLength() throws Exception{
        assertEquals(4, coverage.getHashLength());
    }

    @Test
    public void getHashLengthIfHashEqualZero() throws Exception{
        Set<String> hashes = new HashSet();
        Coverage c = new Coverage(hashes, 6.6);
        assertEquals(0, c.getHashLength());
    }

    @Test
    public void toStringInCoverage() throws Exception{
        String result = coverage.toString();
        assertEquals("Coverage [hashes=[29jz, 29jy, 29jx, 29jv, 29jt, 29jr, 29jq, 29jm], ratio=6.6]", result);
    }


}