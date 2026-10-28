import 'package:flutter/material.dart';
import 'package:mobile/styles/colors.dart';

abstract class AppThemes {
  static final ThemeData standard = ThemeData(
    useMaterial3: true,
    primaryColor: AppColors.pink,
    scaffoldBackgroundColor: AppColors.background,
    appBarTheme: AppBarThemeData(),
    textTheme: TextTheme(),
    buttonTheme: ButtonThemeData(),
    colorScheme: ColorScheme(
      brightness: Brightness.dark,
      primary: AppColors.pink,
      onPrimary: AppColors.textPrimary,
      secondary: AppColors.pink,
      onSecondary: AppColors.textPrimary,
      error: AppColors.red,
      onError: AppColors.textPrimary,
      surface: AppColors.surface,
      onSurface: AppColors.textSecondary,
    ),
  );
}
