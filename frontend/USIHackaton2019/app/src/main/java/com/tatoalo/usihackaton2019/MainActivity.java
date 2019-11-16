package com.tatoalo.usihackaton2019;

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

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;


import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {//implements View.OnClickListener {

    EditText hp, xp;
    ProgressBar hpValue, xpValue;
    ImageButton dataBike, dataBus;
    ImageView playerImage;
    Spinner startData, stopData;
    RequestQueue requestQueue;

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

        //Init Values
        hpValue.setProgress(55, true);
        xpValue.setProgress(65, true);

        Spinner startData = findViewById(R.id.dataStart);
        Spinner stopData = findViewById(R.id.dataStop);
        String[] items = new String[]{"Test1", "Test2", "Test3"};

        ArrayAdapter<String> adapter = new ArrayAdapter<>(this, android.R.layout.simple_spinner_dropdown_item, items);
        startData.setAdapter(adapter);
        stopData.setAdapter(adapter);

        dataBike.setOnClickListener(new Button.OnClickListener() {
            public void onClick(View v) {
                dataBike.setBackgroundResource(R.drawable.btn_border);

            }
        });

        requestQueue= Volley.newRequestQueue(this);

        // ...

        // Instantiate the RequestQueue.
        RequestQueue queue = Volley.newRequestQueue(this);
        String url ="http://private-anon-93fae61792-hackaton4.apiary-mock.com/users/1";

        // Request a string response from the provided URL.
        StringRequest stringRequest = new StringRequest(Request.Method.GET, url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {

                        //print result of the get in case success callback
                        System.out.println(("Here" + response));
                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {

                //print error in case of failed callback
                System.out.println("Errore: " + error.toString() );
            }
        });

        // Add the request to the RequestQueue.
        queue.add(stringRequest);



    }





}
