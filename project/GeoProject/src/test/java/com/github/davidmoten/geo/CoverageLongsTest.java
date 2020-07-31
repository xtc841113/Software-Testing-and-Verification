package com.github.davidmoten.geo;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class CoverageLongsTest {

    private CoverageLongs coverageLongs;
    @Before
    public void setUp() throws Exception {
        coverageLongs = new CoverageLongs(new long[] {75314,75324, 75334, 75344, 75354}, 5, 2.2);
    }

    @After
    public void tearDown() throws Exception {
    }

//    @Test
//    public void getHashes() throws Exception{
//        assertEquals(new long[] {75314,75324, 75334, 75344, 75354}, coverageLongs.getHashes());
//    }

    @Test
    public void getRatio() throws Exception{
        assertEquals(2.2, coverageLongs.getRatio(), 0.001);
    }

    @Test
    public void getCount() throws Exception{
        assertEquals(5, coverageLongs.getCount(), 0.001);
    }

    @Test
    public void getHashLength() throws Exception{
        assertEquals(2,coverageLongs.getHashLength());
    }

    @Test
    public void getHashLengthIfHashEqualZero() throws Exception{
        CoverageLongs c = new CoverageLongs(new long[] {}, 0,3.3);
        assertEquals(0,c.getHashLength());
    }

//    @Test
//    public void toStringInCoverageLongs() throws Exception{
//        String result = coverageLongs.toString();
//        assertEquals("Coverage [hashes=[J@3b95a09c, ratio=2.2]", result);
//    }
}