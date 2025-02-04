package com.example.footballplayers.views;

import android.content.Intent;
import android.os.Bundle;
import android.widget.EditText;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.Observer;

import com.example.footballplayers.R;
import com.example.footballplayers.viewmodels.RegisterViewModel;

public class RegisterActivity extends AppCompatActivity {

    private EditText nameInput, emailInput, passwordInput, confirmPasswordInput, phoneInput, addressInput;
    private RegisterViewModel registerViewModel;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        // Inicializar vistas
        nameInput = findViewById(R.id.nameInput);
        emailInput = findViewById(R.id.emailInput);
        passwordInput = findViewById(R.id.passwordInput);
        confirmPasswordInput = findViewById(R.id.confirmPasswordInput);
        phoneInput = findViewById(R.id.phoneInput);
        addressInput = findViewById(R.id.addressInput);

        // Crear o obtener el ViewModel
        registerViewModel = new RegisterViewModel(getApplication());

        // Observar cambios en los mensajes de error o éxito
        registerViewModel.getErrorMessage().observe(this, new Observer<String>() {
            @Override
            public void onChanged(String message) {
                if (message != null) {
                    Toast.makeText(RegisterActivity.this, message, Toast.LENGTH_SHORT).show();
                    if (message.equals("Usuario registrado exitosamente")) {
                        startActivity(new Intent(RegisterActivity.this, DashboardActivity.class));
                        finish();
                    }
                }
            }
        });

        findViewById(R.id.registerButton).setOnClickListener(v -> {
            String name = nameInput.getText().toString();
            String email = emailInput.getText().toString();
            String password = passwordInput.getText().toString();
            String confirmPassword = confirmPasswordInput.getText().toString();
            String phone = phoneInput.getText().toString();
            String address = addressInput.getText().toString();

            if (registerViewModel.validateInputs(name, email, password, confirmPassword, phone, address)) {
                registerViewModel.registerUser(name, email, password, phone, address);
            }
        });
    }
}
