# =========================================================================
# FILE: api/generate_verdict_pdf.py (REPORTLAB VERSION - CLINICAL DIAGNOSTIC)
# GOAL: Generate Professional Diagnostic Report PDF
# =========================================================================

import json
import base64
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler
from typing import Dict, Any, List
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from io import BytesIO


# --- PROFESSIONAL FOOTER FUNCTION ---
def create_footer_drawer(assessment_id: str):
    """
    Returns a function that draws the professional footer on each page.
    """
    def draw_footer(canvas_obj, doc):
        canvas_obj.saveState()
        
        # Footer text
        footer_text = f"Will I Hate This? — Founder–GTM Misery Risk Diagnostic | Assessment ID: {assessment_id} | Page {doc.page}"
        
        # Draw footer line
        canvas_obj.setStrokeColor(colors.HexColor('#2563eb'))
        canvas_obj.setLineWidth(0.5)
        canvas_obj.line(72, 50, letter[0] - 72, 50)
        
        # Draw footer text
        canvas_obj.setFont('Helvetica', 8)
        canvas_obj.setFillColor(colors.HexColor('#666666'))
        canvas_obj.drawCentredString(letter[0] / 2, 35, footer_text)
        
        canvas_obj.restoreState()
    
    return draw_footer


# --- PDF GENERATION ENGINE (CLINICAL DIAGNOSTIC FORMAT) ---
def generate_verdict_pdf(
    assessment_id: str,
    timestamp: str,
    verdict: Dict[str, Any],
    gtm_shape: str,
    founder_profile: Dict[str, Any],
    mismatch_flags: List[str],
    time_to_regret: str,
    risk_level: str
) -> str:
    """
    Generates a clinical diagnostic report as a Base64-encoded PDF.
    Mirrors the on-screen verdict exactly.
    """
    buffer = BytesIO()
    
    # Create document with custom footer
    doc = SimpleDocTemplate(
        buffer, 
        pagesize=letter, 
        rightMargin=72, 
        leftMargin=72,
        topMargin=72, 
        bottomMargin=60
    )
    
    # Set up the footer callback
    footer_func = create_footer_drawer(assessment_id)
    
    # Container for content
    elements = []
    styles = getSampleStyleSheet()
    
    # Custom styles (clinical, not playful)
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#1f2937'),
        spaceAfter=6,
        alignment=1  # Center
    )
    
    subtitle_style = ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#6b7280'),
        alignment=1,
        spaceAfter=24
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=13,
        textColor=colors.HexColor('#2563eb'),
        spaceAfter=10,
        spaceBefore=16,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#374151'),
        spaceAfter=8,
        leading=14
    )
    
    # --- HEADER ---
    elements.append(Paragraph("FOUNDER–GTM MISERY RISK DIAGNOSTIC", title_style))
    elements.append(Paragraph("Will I Hate This?", subtitle_style))
    
    # --- METADATA ---
    metadata_data = [
        ['Assessment ID:', assessment_id],
        ['Generated:', timestamp],
        ['Assessment Type:', 'Founder–GTM Misery Risk Classification'],
        ['Classification Integrity:', 'Deterministic']
    ]
    metadata_table = Table(metadata_data, colWidths=[2*inch, 4*inch])
    metadata_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#4b5563'))
    ]))
    elements.append(metadata_table)
    elements.append(Spacer(1, 0.15*inch))
    
    # --- DISCLAIMER ---
    disclaimer_text = """
    <i>This assessment does not evaluate idea quality, market size, or likelihood of success. 
    It evaluates the risk that executing the required GTM will conflict with the founder's 
    working preferences.</i>
    """
    elements.append(Paragraph(disclaimer_text, body_style))
    elements.append(Spacer(1, 0.25*inch))
    
    # --- VERDICT BOX ---
    elements.append(Paragraph("VERDICT", heading_style))
    
    # Determine risk color
    risk_colors = {
        'LOW': colors.HexColor('#10b981'),
        'MODERATE': colors.HexColor('#f59e0b'),
        'HIGH': colors.HexColor('#ef4444'),
        'SEVERE': colors.HexColor('#991b1b')
    }
    risk_color = risk_colors.get(risk_level.upper(), colors.black)
    
    verdict_data = [
        [f"Misery Risk: {risk_level.upper()}"],
        ['Expected mismatch between GTM requirements and founder energy profile.']
    ]
    verdict_table = Table(verdict_data, colWidths=[6*inch])
    verdict_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#f9fafb')),
        ('BOX', (0, 0), (-1, -1), 2, risk_color),
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (0, 0), 14),
        ('FONTSIZE', (0, 1), (0, 1), 10),
        ('TEXTCOLOR', (0, 0), (0, 0), risk_color),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('TOPPADDING', (0, 0), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12)
    ]))
    elements.append(verdict_table)
    elements.append(Spacer(1, 0.2*inch))
    
    # --- TIME-TO-REGRET ---
    elements.append(Paragraph(f"Time-to-Regret: {time_to_regret}", heading_style))
    regret_text = """
    This is the point at which founders with similar profiles historically report 
    avoidance, burnout, or abandonment.
    """
    elements.append(Paragraph(regret_text, body_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # --- PRIMARY GTM SHAPE ---
    elements.append(Paragraph("PRIMARY GTM SHAPE", heading_style))
    elements.append(Paragraph(f"<b>{gtm_shape}</b>", body_style))
    
    gtm_description = verdict.get('gtm_description', 'Classification description not available.')
    elements.append(Paragraph(gtm_description, body_style))
    
    # Active Pressure Flags
    pressure_flags = verdict.get('pressure_flags', [])
    if pressure_flags:
        elements.append(Spacer(1, 0.1*inch))
        elements.append(Paragraph("<b>Active Pressure Flags:</b>", body_style))
        for flag in pressure_flags:
            elements.append(Paragraph(f"• {flag}", body_style))
    
    elements.append(Spacer(1, 0.2*inch))
    
    # --- FOUNDER ENERGY PROFILE ---
    elements.append(Paragraph("FOUNDER ENERGY PROFILE", heading_style))
    
    drivers = founder_profile.get('core_drivers', [])
    drains = founder_profile.get('core_drains', [])
    
    if drivers:
        elements.append(Paragraph("<b>Core Drivers:</b>", body_style))
        for driver in drivers:
            elements.append(Paragraph(f"• {driver}", body_style))
    
    if drains:
        elements.append(Spacer(1, 0.1*inch))
        elements.append(Paragraph("<b>Core Drains:</b>", body_style))
        for drain in drains:
            elements.append(Paragraph(f"• {drain}", body_style))
    
    elements.append(Spacer(1, 0.2*inch))
    
    # --- MISMATCH FLAGS ---
    elements.append(Paragraph("MISMATCH FLAGS", heading_style))
    
    if mismatch_flags:
        for flag in mismatch_flags:
            # Use ✗ instead of emoji (PDF-safe)
            flag_text = f"✗ {flag}"
            flag_para = Paragraph(flag_text, body_style)
            elements.append(flag_para)
            elements.append(Spacer(1, 0.05*inch))
    else:
        elements.append(Paragraph("No critical mismatches detected.", body_style))
    
    elements.append(Spacer(1, 0.2*inch))
    
    # --- WHY THIS VERDICT ---
    elements.append(Paragraph("CLASSIFICATION BASIS", heading_style))
    
    explanation = verdict.get('explanation', 'Classification basis not available.')
    elements.append(Paragraph(explanation, body_style))
    
    elements.append(Spacer(1, 0.2*inch))
    
    # --- WHAT THIS VERDICT DOES NOT SAY ---
    elements.append(Paragraph("WHAT THIS VERDICT DOES NOT SAY", heading_style))
    
    does_not_say = """
    This verdict does not say:
    • That the idea is bad
    • That the market is too small
    • That someone else could not succeed with this idea
    • That you should abandon the idea immediately
    
    It only states that this GTM path is statistically misaligned with how you work.
    """
    elements.append(Paragraph(does_not_say, body_style))
    
    elements.append(Spacer(1, 0.3*inch))
    
    # --- FINAL LINE ---
    final_warning = ParagraphStyle(
        'FinalWarning',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#374151'),
        alignment=1,
        fontName='Helvetica-Bold',
        spaceAfter=12
    )
    
    elements.append(Paragraph("Most founders ignore this signal.", final_warning))
    elements.append(Paragraph("The cost is usually paid in time, not money.", final_warning))
    
    elements.append(Spacer(1, 0.2*inch))
    
    # --- IMMUTABILITY NOTICE ---
    immutable_text = """
    <i>This report does not update. Re-running the assessment with different answers 
    constitutes a different idea.</i>
    """
    elements.append(Paragraph(immutable_text, body_style))
    
    # Build PDF with footer
    doc.build(elements, onFirstPage=footer_func, onLaterPages=footer_func)
    
    # Get PDF bytes and encode as base64
    buffer.seek(0)
    pdf_bytes = buffer.read()
    return base64.b64encode(pdf_bytes).decode('utf-8')


# --- HTTP HANDLER (Vercel Serverless Function Format) ---
class handler(BaseHTTPRequestHandler):
    
    def do_OPTIONS(self):
        """Handle CORS preflight requests"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        """Generate PDF diagnostic report"""
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            data = json.loads(body)

            assessment_id = data.get('assessment_id')
            
            if not assessment_id:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'assessment_id is required'}).encode())
                return

            # Generate real-time UTC timestamp
            timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
            
            # Retrieve verdict data
            verdict = data.get('verdict', {})
            gtm_shape = data.get('gtm_shape', 'Not Classified')
            founder_profile = data.get('founder_profile', {})
            mismatch_flags = data.get('mismatch_flags', [])
            time_to_regret = data.get('time_to_regret', 'Unknown')
            risk_level = data.get('risk_level', 'UNKNOWN')
            
            # Validate required data
            if not verdict or not gtm_shape:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                error_response = {'error': 'Verdict data missing. Cannot generate report.'}
                self.wfile.write(json.dumps(error_response).encode())
                print(f"✗ PDF generation failed for assessment {assessment_id}: Missing verdict data")
                return

            # Generate PDF
            pdf_content_base64 = generate_verdict_pdf(
                assessment_id=assessment_id,
                timestamp=timestamp,
                verdict=verdict,
                gtm_shape=gtm_shape,
                founder_profile=founder_profile,
                mismatch_flags=mismatch_flags,
                time_to_regret=time_to_regret,
                risk_level=risk_level
            )
            
            # Return response
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response_data = {
                'success': True,
                'pdfAttachmentData': {
                    'filename': f"WHT-Diagnostic-Report-{assessment_id[:8]}.pdf",
                    'content': pdf_content_base64
                }
            }
            
            self.wfile.write(json.dumps(response_data).encode())
            print(f"✓ PDF generated successfully for assessment: {assessment_id}")

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            error_response = {'error': f'PDF Generation Failed: {str(e)}'}
            self.wfile.write(json.dumps(error_response).encode())
            print(f"✗ PDF generation error: {str(e)}")
