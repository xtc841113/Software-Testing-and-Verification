package com.github.davidmoten.geo.mem;

import com.google.common.base.Optional;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class InfoTest {


    private Info<String, String> info;

    @Before
    public void setUp() throws Exception {
        String id = "e";
        Optional<String> _id = Optional.of(id);
        info = new Info(23.077837,122.115809,3,"c", _id);
    }

    @After
    public void tearDown() throws Exception {
    }

    @Test
    public void id() {
        String id = "e";
        Optional<String> result = Optional.of(id);
        assertEquals(result, info.id());
    }

    @Test
    public void lat() {
        assertEquals(23.077837, info.lat(),0.001);
    }

    @Test
    public void lon() {
        assertEquals(122.115809, info.lon(),0.001);
    }

    @Test
    public void time() {
        assertEquals(3, info.time(),0.001);
    }

    @Test
    public void value() {
        assertEquals("c", info.value());
    }

    @Test
    public void _toString() {
        assertEquals("Info [lat=23.077837, lon=122.115809, time=3, value=c, id=Optional.of(e)]", info.toString());
    }
}