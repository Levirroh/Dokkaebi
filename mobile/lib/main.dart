import 'package:flutter/material.dart';
import 'package:mobile/pages/login_screen.dart';
import 'package:mobile/styles/themes.dart';

void main() {
  runApp(const MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: AppThemes.standard,
      home: LoginScreen(),
    );
  }
}
