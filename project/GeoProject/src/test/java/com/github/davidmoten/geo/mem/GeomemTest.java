package com.github.davidmoten.geo.mem;

import com.google.common.base.Optional;
import com.google.common.base.Predicate;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

public class GeomemTest {

    private Info<String, String> info;
    
    @Before
    public void setUp() throws Exception {
        String id = "e";
        Optional<String> _id = Optional.of(id);
        info = new Info(23.077837,122.115809,3,"c", _id);

        Geomem<String, String> geomem = new Geomem<String, String>();

        geomem.add(info);
        geomem.add(25.0141836,121.4462453,3,"trainStation");
        geomem.add(25.0141836,121.4462453,14,"furniture","ikea");
    }

    @After
    public void tearDown() throws Exception {
    }

    @Test
    public void find_1() {
        Geomem<String, String> geomem = new Geomem<String, String>();
        geomem.add(25.0141836,121.4462453,3,"trainStation");
        geomem.add(25.0141836,121.4462453,14,"furniture","ikea");
        Iterable<Info<String, String>> it = geomem.find(120,
                                                        -120,
                                                        0,
                                                        120,
                                                        -1000000,
                                                        100000);
        assertEquals("[]",it.toString());
    }

    @Test
    public void find_2() {
        Geomem<String, String> geomem = new Geomem<String, String>();
        geomem.add(25.0141836,121.4462453,3,"trainStation");
        geomem.add(25.0141836,121.4462453,14,"furniture","ikea");
        Iterable<Info<String, String>> it = geomem.find(0,0,0,0,-1000000,100000);
        assertEquals("[]",it.toString());
    }

    @Test
    public  void apply_1() {
        Geomem<String, String> geomem = new Geomem<String, String>();
        Predicate<Info<String, String>> p = geomem.createRegionFilter(0,0,0,0);
        assertFalse(p.apply(info));
    }

    @Test
    public  void apply_2() {
        Geomem<String, String> geomem = new Geomem<String, String>();
        Predicate<Info<String, String>> p = geomem.createRegionFilter(13,0,0,13);
        String id1 = "e";
        Optional<String> _id1 = Optional.of(id1);
        Info<String, String> i = new Info(12,12,12,"d",_id1);
        System.out.println(p.apply(i));
        assertTrue(p.apply(i));
    }

}