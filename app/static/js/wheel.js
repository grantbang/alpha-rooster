/**
 * Alpha Rooster - Spin Wheel Game
 * Phase 3.3: Interactive game mechanics
 */

const canvas = document.getElementById('wheelCanvas');
const ctx = canvas.getContext('2d');
const spinButton = document.getElementById('spinButton');
const resultDiv = document.getElementById('result');
const resultText = document.getElementById('resultText');

// Wheel configuration - savings tiers
const segments = [
    { label: 'BRONZE', color: '#cd7f32', tier: 'Bronze' },
    { label: 'SILVER', color: '#95a5a6', tier: 'Silver' },
    { label: 'GOLD',   color: '#f1c40f', tier: 'Gold'   },
    { label: 'BRONZE', color: '#cd7f32', tier: 'Bronze' },
    { label: 'SILVER', color: '#95a5a6', tier: 'Silver' },
    { label: 'GOLD',   color: '#f1c40f', tier: 'Gold'   },
];

const numSegments = segments.length;
const segmentAngle = (2 * Math.PI) / numSegments;
let currentRotation = 0;
let isSpinning = false;

// Draw the wheel
function drawWheel() {
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    const radius = 180;

    for (let i = 0; i < numSegments; i++) {
        const angle = currentRotation + i * segmentAngle;

        // Draw segment
        ctx.beginPath();
        ctx.arc(centerX, centerY, radius, angle, angle + segmentAngle);
        ctx.lineTo(centerX, centerY);
        ctx.fillStyle = segments[i].color;
        ctx.fill();
        ctx.strokeStyle = '#fff';
        ctx.lineWidth = 3;
        ctx.stroke();

        // Draw text
        ctx.save();
        ctx.translate(centerX, centerY);
        ctx.rotate(angle + segmentAngle / 2);
        ctx.textAlign = 'center';
        ctx.fillStyle = '#fff';
        ctx.font = 'bold 16px Arial';
        ctx.fillText(segments[i].label, radius / 1.5, 6);
        ctx.restore();
    }

    // Draw center circle
    ctx.beginPath();
    ctx.arc(centerX, centerY, 20, 0, 2 * Math.PI);
    ctx.fillStyle = '#fff';
    ctx.fill();
    ctx.strokeStyle = '#333';
    ctx.lineWidth = 3;
    ctx.stroke();

    // Draw pointer (triangle at top)
    ctx.beginPath();
    ctx.moveTo(centerX - 15, 20);
    ctx.lineTo(centerX + 15, 20);
    ctx.lineTo(centerX, 50);
    ctx.closePath();
    ctx.fillStyle = '#e74c3c';
    ctx.fill();
    ctx.strokeStyle = '#c0392b';
    ctx.lineWidth = 2;
    ctx.stroke();
}

// Spin the wheel
function spinWheel() {
    if (isSpinning) return;

    isSpinning = true;
    spinButton.disabled = true;
    spinButton.textContent = 'SPINNING...';
    resultDiv.classList.remove('show');

    // Track spin event with Meta Pixel
    if (typeof fbq !== 'undefined') {
        fbq('trackCustom', 'SpinWheel', {
            content_name: 'Wheel Spin',
            value: 1
        });
        console.log('Meta Pixel: SpinWheel custom event tracked');
    }

    // Random spin (5-7 full rotations + random angle)
    const spins = 5 + Math.random() * 2;
    const finalRotation = spins * 2 * Math.PI + Math.random() * 2 * Math.PI;
    const duration = 3000; // 3 seconds
    const startTime = Date.now();
    const startRotation = currentRotation;

    function animate() {
        const elapsed = Date.now() - startTime;
        const progress = Math.min(elapsed / duration, 1);

        // Easing function (ease-out)
        const easeOut = 1 - Math.pow(1 - progress, 3);
        currentRotation = startRotation + finalRotation * easeOut;

        // Clear and redraw
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        drawWheel();

        if (progress < 1) {
            requestAnimationFrame(animate);
        } else {
            // Spin complete
            const winningSegment = getWinningSegment();
            showResult(winningSegment);
        }
    }

    animate();
}

// Determine which segment won
function getWinningSegment() {
    // The pointer is at the top, so we need to find which segment is pointing up
    const normalizedRotation = (currentRotation % (2 * Math.PI) + 2 * Math.PI) % (2 * Math.PI);
    const pointerAngle = (2 * Math.PI - normalizedRotation + Math.PI / 2) % (2 * Math.PI);
    const segmentIndex = Math.floor(pointerAngle / segmentAngle) % numSegments;
    return segments[segmentIndex];
}

// Show result with confetti
function showResult(segment) {
    isSpinning = false;

    // Fire confetti
    confetti({
        particleCount: 150,
        spread: 70,
        origin: { y: 0.6 },
        colors: [segment.color, '#fff', '#ffd700']
    });

    // Show result
    const tierColors = { 'Gold': '#f39c12', 'Silver': '#7f8c8d', 'Bronze': '#cd7f32' };
    const tierColor = tierColors[segment.tier] || '#27ae60';
    resultText.innerHTML = `
        <strong style="font-size: 36px; color: ${tierColor};">
            🏆 ${segment.tier} Savings Tier
        </strong><br/>
        <span style="font-size: 18px; color: #2c3e50; display: block; margin: 10px 0;">
            You qualified for a <strong>${segment.tier} level</strong> quote — drivers in your area are saving!
        </span>
        <span style="font-size: 14px; color: #7f8c8d;">
            Claim your free quote below — takes 60 seconds, no SSN required.
        </span>
    `;
    resultDiv.classList.add('show');

    console.log(`User won: ${segment.tier} tier`);
}

// Initialize
drawWheel();

// Event listeners
spinButton.addEventListener('click', spinWheel);
