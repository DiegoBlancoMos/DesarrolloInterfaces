package com.example.footballplayers.repositories;

import com.example.footballplayers.models.User;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import android.util.Log;

public class UserRepository {

    private FirebaseAuth mAuth;
    private DatabaseReference mDatabase;

    public UserRepository() {
        mAuth = FirebaseAuth.getInstance();
        mDatabase = FirebaseDatabase.getInstance().getReference();
    }

    // Registrar un usuario en Firebase Authentication
    public void registerUser(String email, String password, final User user, final UserRepositoryCallback callback) {
        mAuth.createUserWithEmailAndPassword(email, password)
                .addOnCompleteListener(task -> {
                    if (task.isSuccessful()) {
                        FirebaseUser firebaseUser = mAuth.getCurrentUser();
                        if (firebaseUser != null) {
                            saveUserData(firebaseUser.getUid(), user, callback);
                        } else {
                            callback.onFailure("Error: No se pudo obtener el usuario autenticado");
                        }
                    } else {
                        callback.onFailure(task.getException() != null ? task.getException().getMessage() : "Error desconocido");
                    }
                });
    }
    public void loginUser(String email, String password, final UserRepositoryCallback callback) {
        mAuth.signInWithEmailAndPassword(email, password)
                .addOnCompleteListener(task -> {
                    if (task.isSuccessful()) {
                        callback.onSuccess();
                    } else {
                        callback.onFailure(task.getException() != null ? task.getException().getMessage() : "Error desconocido");
                    }
                });
    }
    // Guardar los datos del usuario en Firebase Database
    private void saveUserData(String userId, User user, final UserRepositoryCallback callback) {
        mDatabase.child("users").child(userId).setValue(user)
                .addOnCompleteListener(task -> {
                    if (task.isSuccessful()) {
                        callback.onSuccess();
                    } else {
                        callback.onFailure(task.getException() != null ? task.getException().getMessage() : "Error desconocido");
                    }
                });
    }

    // Interfaz para callback
    public interface UserRepositoryCallback {
        void onSuccess();
        void onFailure(String error);
    }
}
