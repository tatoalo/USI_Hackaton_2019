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
import com.loopj.android.http.*;

import org.json.*;
import com.loopj.android.http.*;

import cz.msebera.android.httpclient.Header;


import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {//implements View.OnClickListener {

    EditText hp, xp;
    ProgressBar hpValue, xpValue;
    ImageButton dataBike, dataBus;
    ImageView playerImage;
    Spinner startData, stopData;

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

        //AsyncHttpClient myClient = new AsyncHttpClient();





    }





}
