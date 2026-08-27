
import 'package:flutter/material.dart';

void main() {
  runApp(const SignalMasterApp());
}

class SignalMasterApp extends StatelessWidget {
  const SignalMasterApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Signal Master 5.0',
      theme: ThemeData.dark(useMaterial3: true),
      home: const DashboardPage(),
    );
  }
}

class DashboardPage extends StatelessWidget {
  const DashboardPage({super.key});

  @override
  Widget build(BuildContext context) {
    const markets = ['EUR/USD', 'BTC/USD', 'NAS100'];
    return Scaffold(
      appBar
