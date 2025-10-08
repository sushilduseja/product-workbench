# Customer Journey Mapper — Demo Guide

## 🚀 Quick Start

### Prerequisites
- Node.js 16+ installed
- Git installed
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Installation & Setup

```bash
# (Optional) Clone the demo source for local development
git clone https://github.com/sushilduseja/customer-journey-mapper.git
cd customer-journey-mapper

# Install dependencies and run
npm install
npm run dev
```

**Open your browser to (local):** `http://localhost:5173`

**Live hosted demo (no local setup required):** https://customer-journey-mapper.netlify.app/

Useful anchors:
- Features: https://customer-journey-mapper.netlify.app/#features
- Metrics/Impact: https://customer-journey-mapper.netlify.app/#metrics
- Architecture: https://customer-journey-mapper.netlify.app/#architecture

---

## 🎯 Demo Scenarios

### Scenario 1: Fintech Onboarding Journey
**Objective:** Map and optimize a typical fintech user onboarding flow

**Steps:**
1. **Create New Journey Map**
   - Click "New Journey" button
   - Select "Fintech Onboarding" template
   - Name your journey: "Demo Fintech Flow"

2. **Build the Journey**
   - Drag "Account Creation" to center stage
   - Add "Email Verification" → "KYC Verification" → "First Deposit"
   - Connect stages with auto-flowing lines

3. **Add Friction Points**
   - Click on "KYC Verification" stage
   - Set drop-off rate to 47%
   - Add user feedback: "Too many documents required"

4. **Create A/B Test**
   - Click "Create Variant" on KYC stage
   - Simplify the flow (reduce steps)
   - Set Variant B drop-off to 22%

5. **View Results**
   - Click "Run Experiment"
   - Watch animated metrics show improvement
   - Export presentation-ready map

### Scenario 2: E-commerce Checkout Flow
**Objective:** Identify and fix checkout abandonment issues

**Steps:**
1. **Import E-commerce Template**
   - Select "E-commerce Checkout" from template gallery
   - Customize for your specific flow

2. **Add Analytics Data**
   - Import conversion rates from Google Analytics
   - Add user feedback from support tickets
   - Set up real-time monitoring

3. **Identify Bottlenecks**
   - Use heatmapping to find friction points
   - Analyze user comments for common issues
   - Prioritize fixes by impact

4. **Test Optimizations**
   - Create checkout variants
   - A/B test different approaches
   - Measure conversion improvements

---

## 🛠️ Technical Implementation

### Local Development

```bash
# Development mode with hot reload
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run tests
npm run test

# Lint code
npm run lint
```

### Project Structure

```
src/
├── components/          # React components
│   ├── Canvas/         # Journey mapping canvas
│   ├── Analytics/      # Real-time analytics
│   └── Experiments/   # A/B testing framework
├── hooks/              # Custom React hooks
├── utils/              # Utility functions
├── types/              # TypeScript type definitions
└── assets/             # Static assets
```

### Key Technologies

- **Frontend Framework:** React 18 + TypeScript
- **Build Tool:** Vite (fast development & builds)
- **Styling:** CSS Modules + CSS Variables
- **State Management:** React Context + useReducer
- **Canvas Rendering:** HTML5 Canvas API
- **Analytics:** Custom real-time data processing

---

## 📊 Data Integration

### Supported Data Sources

#### Analytics Platforms
- **Google Analytics 4**
  ```javascript
  // Example integration
  const ga4Data = await fetchGA4Data({
    propertyId: 'your-property-id',
    startDate: '2024-01-01',
    endDate: '2024-01-31'
  });
  ```

- **Mixpanel**
  ```javascript
  // Example integration
  const mixpanelData = await fetchMixpanelData({
    projectId: 'your-project-id',
    events: ['page_view', 'conversion']
  });
  ```

#### User Feedback Tools
- **Hotjar:** Heatmap and session recording data
- **Zendesk:** Support ticket analysis
- **Intercom:** User message sentiment analysis

#### A/B Testing Platforms
- **Custom Framework:** Built-in experimentation engine
- **Optimizely:** External A/B testing integration
- **VWO:** Visual website optimizer data

### Data Format

```typescript
interface JourneyData {
  stages: JourneyStage[];
  connections: Connection[];
  metrics: StageMetrics[];
  feedback: UserFeedback[];
  experiments: Experiment[];
}

interface JourneyStage {
  id: string;
  name: string;
  type: 'action' | 'decision' | 'wait';
  metrics: {
    conversionRate: number;
    dropOffRate: number;
    avgTimeSpent: number;
  };
}
```

---

## 🎨 Customization Guide

### Creating Custom Templates

1. **Define Template Structure**
   ```typescript
   const customTemplate = {
     name: "SaaS Onboarding",
     stages: [
       { name: "Sign Up", type: "action" },
       { name: "Email Verification", type: "action" },
       { name: "Profile Setup", type: "action" },
       { name: "First Feature Use", type: "action" }
     ],
     connections: [
       { from: "Sign Up", to: "Email Verification" },
       { from: "Email Verification", to: "Profile Setup" },
       { from: "Profile Setup", to: "First Feature Use" }
     ]
   };
   ```

2. **Add Custom Metrics**
   ```typescript
   const customMetrics = {
     conversionRate: 0.85,
     dropOffRate: 0.15,
     avgTimeSpent: 300, // seconds
     userSatisfaction: 4.2
   };
   ```

3. **Configure A/B Tests**
   ```typescript
   const abTest = {
     name: "Simplified Onboarding",
     variants: [
       { name: "Original", conversionRate: 0.75 },
       { name: "Simplified", conversionRate: 0.89 }
     ],
     duration: 14, // days
     significance: 0.95
   };
   ```

### Styling Customization

```css
/* Custom theme variables */
:root {
  --primary-color: #3b82f6;
  --secondary-color: #10b981;
  --danger-color: #ef4444;
  --warning-color: #f59e0b;
  --canvas-bg: #f8fafc;
  --stage-bg: #ffffff;
  --connection-color: #6b7280;
}

/* Custom stage styling */
.journey-stage {
  background: var(--stage-bg);
  border: 2px solid var(--primary-color);
  border-radius: 8px;
  padding: 16px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
```

---

## 🔧 Troubleshooting

### Common Issues

#### Development Server Won't Start
```bash
# Clear node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
npm run dev
```

#### Canvas Not Rendering
- Check browser console for errors
- Ensure modern browser with Canvas support
- Verify JavaScript is enabled

#### Data Import Issues
- Check API credentials and permissions
- Verify data format matches expected schema
- Check network connectivity and CORS settings

#### Performance Issues
- Reduce number of stages in complex journeys
- Optimize data queries and pagination
- Use browser dev tools to identify bottlenecks

### Debug Mode

```bash
# Enable debug logging
DEBUG=true npm run dev

# Verbose analytics logging
ANALYTICS_DEBUG=true npm run dev
```

---

## 📈 Performance Optimization

### Best Practices

1. **Journey Complexity**
   - Keep stages under 20 for optimal performance
   - Use pagination for large datasets
   - Implement lazy loading for complex visualizations

2. **Data Management**
   - Cache frequently accessed data
   - Use debouncing for real-time updates
   - Implement data compression for large datasets

3. **Rendering Optimization**
   - Use React.memo for expensive components
   - Implement virtual scrolling for long lists
   - Optimize canvas rendering with requestAnimationFrame

---

## 🚀 Deployment

### Netlify Deployment

```bash
# Build for production
npm run build

# Deploy to Netlify
netlify deploy --prod --dir=dist
```

### Vercel Deployment

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel --prod
```

### Docker Deployment

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "run", "preview"]
```

---

## 📚 Additional Resources

- **📖 [Case Study](./case-study.md)** - Detailed implementation analysis
- **🎨 [Visual Gallery](../visuals/)** - Screenshots and demos
- **📊 [Impact Metrics](../impact/metrics.md)** - Performance data
- **💬 [Testimonials](../impact/testimonials.md)** - User feedback

---

Live demo: https://customer-journey-mapper.netlify.app/ (see anchors listed above)

---

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

### Code Standards
- Use TypeScript for type safety
- Follow React best practices
- Write comprehensive tests
- Document new features

---

*Ready to transform your user journey insights into actionable intelligence? Start with the demo scenarios above and customize for your specific use case.*
