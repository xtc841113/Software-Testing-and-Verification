package com.github.davidmoten.geo;

import com.google.common.escape.Escaper;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class LatLongTest {

    @Before
    public void setUp() throws Exception {
    }

    @After
    public void tearDown() throws Exception {
    }

    @Test
    public void toStringInLatLong() throws Exception {
        LatLong l = new LatLong(1.1, 2.2);
        String result = l.add(3.3, 4.4).toString();

        LatLong expectedValue = new LatLong(4.4, 6.6000000000000005);

        assertEquals(expectedValue.toString(), result);
    }


}