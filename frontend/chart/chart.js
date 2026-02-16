const canvas = document.getElementById("priceChart");
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth * 0.75;
canvas.height = window.innerHeight;


let bars = [];
let icebergs = [];

// Fetch real chart data from backend API
async function fetchChartData() {
    try {
        const res = await fetch('/api/v1/chart', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                symbol: 'GC=F',
                interval: '5m',
                bars: 100,
                include_levels: true,
                include_icebergs: true
            })
        });
        if (!res.ok) throw new Error('Failed to fetch chart data');
        const data = await res.json();
        bars = (data.bars || []).map(bar => ({
            open: bar.open,
            high: bar.high,
            low: bar.low,
            close: bar.close,
            volume: bar.volume
        }));
        icebergs = data.iceberg_zones || [];
        draw();
    } catch (e) {
        console.error('Chart fetch error:', e);
    }
}

// Poll for live updates every 5 seconds
setInterval(fetchChartData, 5000);
fetchChartData();

function draw() {
    ctx.clearRect(0,0,canvas.width,canvas.height);
    bars.forEach((bar, i) => {
        const x = i * 8;
        const yOpen = mapPrice(bar.open);
        const yClose = mapPrice(bar.close);
        const yHigh = mapPrice(bar.high);
        const yLow = mapPrice(bar.low);
        // Candle
        ctx.strokeStyle = bar.close > bar.open ? "#3cff9e" : "#ff4d4d";
        ctx.beginPath();
        ctx.moveTo(x, yHigh);
        ctx.lineTo(x, yLow);
        ctx.stroke();
        // Body
        ctx.fillRect(x-2, Math.min(yOpen,yClose), 4, Math.abs(yOpen-yClose));
        // Volume (quantity)
        ctx.fillStyle = "#888";
        ctx.fillRect(x-2, canvas.height-50, 4, bar.volume / 10);
    });
    icebergs.forEach(z => {
        ctx.fillStyle = z.side === "BUY" ? "rgba(0,255,0,0.15)" : "rgba(255,0,0,0.15)";
        ctx.fillRect(0, mapPrice(z.price)-6, canvas.width, 12);
    });
}

function mapPrice(p) {
    return canvas.height - (p * 0.4);
}

draw(); // Initial draw
// TODO: Add WebSocket or polling to update bars/icebergs and call draw()
