package com.example.footballplayers;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

public class RegisterActivity extends AppCompatActivity {
    private FirebaseAuth mAuth;
    private DatabaseReference mDatabase;

    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        mAuth = FirebaseAuth.getInstance();
        mDatabase = FirebaseDatabase.getInstance().getReference();

        // Inicializar vistas
        EditText nameInput = findViewById(R.id.nameInput);
        EditText emailInput = findViewById(R.id.emailInput);
        EditText passwordInput = findViewById(R.id.passwordInput);
        EditText confirmPasswordInput = findViewById(R.id.confirmPasswordInput);
        EditText phoneInput = findViewById(R.id.phoneInput);
        EditText addressInput = findViewById(R.id.addressInput);
        Button registerButton = findViewById(R.id.registerButton);

        registerButton.setOnClickListener(v -> {
            if (validateInputs()) {
                registerUser();
            }
        });
    }


    private boolean validateInputs() {
        // Validación de campos
        String password = passwordInput.getText().toString();
        String confirmPassword = confirmPasswordInput.getText().toString();

        if (!password.equals(confirmPassword)) {
            Toast.makeText(this, "Las contraseñas no coinciden", Toast.LENGTH_SHORT).show();
            return false;
        }

        // Validar que ningún campo esté vacío
        if (nameInput.getText().toString().isEmpty() ||
                emailInput.getText().toString().isEmpty() ||
                phoneInput.getText().toString().isEmpty() ||
                addressInput.getText().toString().isEmpty()) {
            Toast.makeText(this, "Todos los campos son obligatorios", Toast.LENGTH_SHORT).show();
            return false;
        }

        return true;
    }

    private void registerUser() {
        String email = emailInput.getText().toString();
        String password = passwordInput.getText().toString();

        mAuth.createUserWithEmailAndPassword(email, password)
                .addOnCompleteListener(task -> {
                    if (task.isSuccessful()) {
                        FirebaseUser user = mAuth.getCurrentUser();
                        saveUserData(user.getUid());
                    } else {
                        Toast.makeText(RegisterActivity.this, "Error en el registro: " +
                                task.getException().getMessage(), Toast.LENGTH_SHORT).show();
                    }
                });
    }

    private void saveUserData(String userId) {
        User user = new User(
                nameInput.getText().toString(),
                emailInput.getText().toString(),
                phoneInput.getText().toString(),
                addressInput.getText().toString()
        );

        mDatabase.child("users").child(userId).setValue(user)
                .addOnCompleteListener(task -> {
                    if (task.isSuccessful()) {
                        startActivity(new Intent(RegisterActivity.this, DashboardActivity.class));
                        finish();
                    } else {
                        Toast.makeText(RegisterActivity.this, "Error al guardar datos",
                                Toast.LENGTH_SHORT).show();
                    }
                });
    }
}