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
      appBar: AppBar(
        title: const Text('SIGNAL MASTER 5.0'),
        actions: [
          IconButton(
            icon: const Icon(Icons.settings),
            onPressed: () => Navigator.push(
              context,
              MaterialPageRoute(builder: (_) => const SettingsPage()),
            ),
          ),
        ],
      ),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          const Text('MARKET INTELLIGENCE',
              style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
          const SizedBox(height: 16),
          for (final market in markets)
            Card(
              child: ListTile(
                title: Text(market),
                subtitle: const Text('WAIT • DATA STATUS: BLOCKED'),
                trailing: const Icon(Icons.pause_circle_outline),
                onTap: () => Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => MarketPage(symbol: market),
                  ),
                ),
              ),
            ),
        ],
      ),
    );
  }
}

class MarketPage extends StatelessWidget {
  final String symbol;
  const MarketPage({super.key, required this.symbol});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(symbol)),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: const [
          AspectRatio(
            aspectRatio: 16 / 9,
            child: Center(child: Text('INTERACTIVE CANDLE CHART\n\n'
                'Pan • Zoom • Timeframes • AI overlays')),
          ),
          SizedBox(height: 16),
          Text('MARKET STATE'),
          Text('WAIT — verified live data required'),
          SizedBox(height: 16),
          Text('SCENARIOS'),
          Text('Bullish • Bearish • Neutral'),
          SizedBox(height: 16),
          Text('WHY NOT NOW?'),
          Text('• Live market data is not configured'),
          Text('• A+ gate is blocked'),
        ],
      ),
    );
  }
}

class SettingsPage extends StatelessWidget {
  const SettingsPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Connections & Settings')),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: const [
          Text('MARKET DATA'),
          TextField(decoration: InputDecoration(labelText: 'Provider')),
          TextField(decoration: InputDecoration(labelText: 'API/App ID')),
          TextField(decoration: InputDecoration(labelText: 'API Token')),
          SizedBox(height: 16),
          Text('GEMINI AI'),
          TextField(decoration: InputDecoration(labelText: 'API Key')),
          SizedBox(height: 16),
          Text('NEWS'),
          TextField(decoration: InputDecoration(labelText: 'API Key')),
          SizedBox(height: 16),
          Text('TELEGRAM'),
          TextField(decoration: InputDecoration(labelText: 'Bot Token')),
          TextField(decoration: InputDecoration(labelText: 'Chat ID')),
        ],
      ),
    );
  }
}
