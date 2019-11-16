package com.tatoalo.usihackaton2019;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.AsyncTask;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.ProgressBar;
import android.widget.Spinner;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.squareup.picasso.Picasso;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import org.json.JSONTokener;


import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {//implements View.OnClickListener {

    EditText hp, xp;
    ProgressBar hpValue, xpValue;
    ImageButton dataBike, dataBus;
    ImageView playerImage;
    Spinner startData, stopData;
    RequestQueue requestQueue;
    String hpValueString = "50", xpValueString = "50", maxValueXp = "";
    List<String> bikeAddresses = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        hp = (EditText) findViewById(R.id.hp);
        xp = (EditText) findViewById(R.id.xp);

        hpValue = (ProgressBar) findViewById(R.id.hpValue);
        xpValue = (ProgressBar) findViewById(R.id.xpValue);

        hp.setFocusable(false);
        xp.setFocusable(false);
        hpValue.setFocusable(false);
        xpValue.setFocusable(false);

        dataBike = (ImageButton) findViewById(R.id.dataTypeBike);
        dataBike.setImageResource(R.drawable.bike);
        dataBus = (ImageButton) findViewById(R.id.dataTypeBus);

        playerImage = (ImageView) findViewById(R.id.playerImg);

        System.out.println("CIAO");
        //Init Values
        hpValue.setProgress(Integer.parseInt(hpValueString), true);
        xpValue.setProgress(Integer.parseInt(xpValueString), true);

        //Spinner startData = findViewById(R.id.dataStart);
        //Spinner stopData = findViewById(R.id.dataStop);
        String[] items = new String[]{"Test1", "Test2", "Test3"};

        final ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_spinner_dropdown_item, bikeAddresses);
        //startData.setAdapter(adapter);
        //stopData.setAdapter(adapter);

        dataBike.setOnClickListener(new Button.OnClickListener() {
            public void onClick(View v) {
                dataBike.setBackgroundResource(R.drawable.btn_border);

            }
        });

        requestQueue= Volley.newRequestQueue(this);

        // Instantiate the RequestQueue.
        RequestQueue queue = Volley.newRequestQueue(this);
        String urlUsers = "http://private-anon-93fae61792-hackaton4.apiary-mock.com/users/1";
        String urlBikes = "http://private-anon-5ec2e8c39d-hackaton4.apiary-mock.com/stations/bike";

        // GET USERS
        StringRequest stringRequestUsers = new StringRequest(Request.Method.GET, urlUsers,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {

                        //System.out.println(("Here" + response));

                        try {
                            JSONObject json= (JSONObject) new JSONTokener(response).nextValue();
                            JSONObject json2 = json.getJSONObject("stats");
                            hpValueString = (String) json2.get("hp");
                            xpValueString = (String) json2.get("xp");
                            maxValueXp = (String) json2.get("xp_required");

                            xpValue.setMax(Integer.parseInt(maxValueXp));

                            hpValue.setProgress(Integer.parseInt(hpValueString), true);
                            xpValue.setProgress(Integer.parseInt(xpValueString), true);

                            String urlImage = (String) json.get("icon");

                            //Picasso.get().load(urlImage).into(playerImage);

                        } catch (JSONException e) {
                            e.printStackTrace();
                        }

                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                //print error in case of failed callback
                System.out.println("Errore: " + error.toString() );
            }
        });


        //GET BIKES
        StringRequest stringRequestBikes = new StringRequest(Request.Method.GET, urlBikes,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {

                        int count = 0;


                            try {
                                JSONArray json = new JSONArray(response);
                                //System.out.println(json.getJSONObject(count));

                                while(count < json.length()){
                                    //System.out.println(json.getJSONObject(count).get("address"));
                                    bikeAddresses.add(json.getJSONObject(count).get("address").toString());
                                    count++;

                                }

                                /*ArrayAdapter<String> dataAdapter = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_dropdown_item, bikeAddresses);
                                dataAdapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
                                spinner2.setAdapter(dataAdapter);*/
                                Spinner startData = findViewById(R.id.dataStart);
                                Spinner stopData = findViewById(R.id.dataStop);

                                startData.setAdapter(adapter);
                                stopData.setAdapter(adapter);




                            } catch (JSONException e) {
                                e.printStackTrace();
                            }



                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                //print error in case of failed callback
                System.out.println("Errore: " + error.toString() );
            }
        });

        // Add the request to the RequestQueue.
        queue.add(stringRequestUsers);
        queue.add(stringRequestBikes);


    }



}
