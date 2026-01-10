# Will I Hate This?

> Ship fast. But ship smart.

A tool that predicts if your idea's go-to-market (GTM) strategy matches how you actually work—before you build something great that requires what you hate doing.

**🚀 Live Site:** [Coming Soon]  
**📧 Join Waitlist:** [Coming Soon]

---

## 🎯 The Problem

Standard idea validation asks:
- ✅ Is there a market?
- ✅ Will people pay?
- ✅ Can you build it?

But it doesn't ask:
- ❌ Will the required GTM make you miserable?
- ❌ How long until you discover the mismatch?
- ❌ Are you building the right idea for the wrong person (you)?

**Result:** Builders create products that work—but require distribution strategies they hate. They discover this 60-90 days in, after committing time and energy.

---

## 💡 The Solution

**Will I Hate This?** helps you predict persona/GTM mismatch before you build.

### Three Core Questions:

1. **What does this idea's GTM actually require?**
   - Trust building timeline? Sales calls? Content volume? Partnership complexity?

2. **What will YOU actually do?**
   - What energizes you? What drains you? What's sustainable?

3. **Where's the potential mismatch?**
   - Specific incompatibilities, realistic timelines, alternative strategies

**Not "Don't ship." But "Ship with clear eyes about what comes next."**

---

## 🛠️ Tech Stack

### Current (Landing Page Phase)
- **Frontend:** Next.js 14 (App Router) + React
- **Styling:** Tailwind CSS
- **Hosting:** Vercel (free tier)
- **Email:** Resend (waitlist collection)
- **Marketing:** Loops.so (email nurture)
- **Version Control:** GitHub

### Future (Post-Validation)
- **Database:** Supabase (free tier)
- **AI Analysis:** Claude API or Gemini (pay-per-use)
- **Analytics:** Vercel Analytics or Plausible

**Total upfront cost: $0-12** (domain only)

---

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- npm or yarn
- Resend API key (free tier: 3,000 emails/month)

### Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/will-i-hate-this.git
cd will-i-hate-this

# Install dependencies
npm install

# Set up environment variables
cp .env.example .env.local
# Add your RESEND_API_KEY to .env.local

# Run development server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Deploy to Vercel

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel

# Add environment variables in Vercel dashboard
# RESEND_API_KEY=your_key_here
```

---

## 📁 Project Structure

```
will-i-hate-this/
├── app/
│   ├── page.tsx              # Landing page (waitlist phase)
│   ├── api/
│   │   └── waitlist/
│   │       └── route.ts      # Waitlist API endpoint
│   └── layout.tsx            # Root layout
├── components/
│   └── LandingPage.tsx       # Main landing page component
├── public/
│   └── favicon.ico           # Compass + alert icon
├── .env.example              # Environment variables template
├── .env.local                # Your local environment (gitignored)
├── package.json
├── tailwind.config.js
└── README.md
```

---

## 🔧 API Integration

### Waitlist Endpoint

**Endpoint:** `POST /api/waitlist`

**Request Body:**
```json
{
  "email": "user@example.com"
}
```

**Response:**
```json
{
  "success": true,
  "message": "Added to waitlist"
}
```

### Resend Integration Example

```typescript
// app/api/waitlist/route.ts
import { Resend } from 'resend';

const resend = new Resend(process.env.RESEND_API_KEY);

export async function POST(request: Request) {
  const { email } = await request.json();
  
  // Send confirmation email
  await resend.emails.send({
    from: 'hello@willihatethis.com',
    to: email,
    subject: 'You\'re on the waitlist!',
    html: '<p>Thanks for joining. Updates coming soon.</p>'
  });
  
  // Optional: Add to Loops.so for nurture sequence
  // await fetch('https://app.loops.so/api/v1/contacts/create', {
  //   method: 'POST',
  //   headers: { 'Authorization': `Bearer ${process.env.LOOPS_API_KEY}` },
  //   body: JSON.stringify({ email })
  // });
  
  return Response.json({ success: true });
}
```

---

## 📊 Validation Metrics

### Phase 1: Waitlist (Week 1-4)

**Success Criteria:**
- ✅ **100+ signups** = Strong interest, build MVP
- ⚠️ **50-99 signups** = Medium interest, interview 10 people
- ❌ **<50 signups** = Weak interest, reconsider or pivot

**Key Signals:**
- Reddit post engagement (comments, upvotes)
- "Share Your Story" submissions
- Email open rates (if follow-ups sent)

### Phase 2: MVP (If Validated)

**Success Criteria:**
- ✅ **5+ paid users in 30 days** = Continue development
- ⚠️ **10+ free users, 0 paid** = Pricing problem
- ❌ **<10 total users** = Distribution problem

---

## 🎨 Design Principles

### Colors
- **Primary:** Deep Blue (`#2563eb`)
- **Secondary:** Amber/Orange (`#f59e0b`) - for warnings
- **Accent:** Emerald (`#10b981`) - for success
- **Background:** Off-white (`#fafafa`)
- **Text:** Near-black (`#1f2937`)

### Typography
- **Headings:** Inter or Geist (Vercel default)
- **Body:** System fonts (`-apple-system, sans-serif`)

### Mascot
- Compass with alert icon
- Represents: "Navigate away from mismatches"
- Clean, professional, not overly playful

---

## 📝 Content Philosophy

### We Support "Ship Fast"
- ✅ Shipping quickly to learn
- ✅ Building in public
- ✅ Testing before perfecting
- ✅ Learning from failures

### We Just Add One Question
**Before you ship: "Does the GTM this idea requires match what you're actually willing to do?"**

Not "Don't ship." But "Ship with clear eyes about what comes next."

---

## 🤝 Contributing

This is currently a solo project in validation phase. Once validated, contributions welcome for:

- Pattern library expansion (GTM requirements database)
- Post-mortem case studies
- Alternative GTM strategies
- UI/UX improvements

---

## 📖 The Origin Story

I spent 60 days building [FreelancerHealth](https://freelancerhealth.co)—a tax calculator implementing IRS Publication 974's iterative method for self-employed health insurance deductions.

The product works. The math is correct. Users love it.

But I discovered too late that the GTM requires:
- 18 months of trust building (drains me)
- CPA partnership development (uncomfortable)
- Demo calls with tax firms (I avoid this)

I didn't waste those 60 days—I learned a ton.

**I just wish I'd known the GTM requirements BEFORE I committed.**

This tool is for builders like me: logic-systematizers who hate wasting time on structurally wrong ideas.

---

## 📬 Contact

- **Email:** hello@willihatethis.com
- **Twitter:** [@yourusername](https://twitter.com/yourusername)
- **GitHub:** [@yourusername](https://github.com/yourusername)

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

---

## 🙏 Acknowledgments

Built with support from:
- The "ship it fast" community (we're with you!)
- Logic-systematizers who value their time
- Builders who've shared their post-mortems

**For builders who ship fast—but want to know what comes after shipping.**

---

**Status:** 🚧 Pre-launch (Waitlist Phase)  
**Last Updated:** January 2025
