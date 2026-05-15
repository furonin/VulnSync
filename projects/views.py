from django.shortcuts import render, redirect
from .models import Project
from .utils import parse_nmap_xml
from django.http import HttpResponse
from .utils import generate_assessment_report

def upload_scan(request):
    """
    Handles Nmap XML file uploads and triggers the parsing engine.
    """
    if request.method == 'POST' and request.FILES.get('nmap_file'):
        nmap_file = request.FILES['nmap_file']
        project_id = request.POST.get('project_id')
        
        # Trigger the parser utility
        success = parse_nmap_xml(nmap_file, project_id)
        
        if success:
            # Redirect to admin to see the results for now
            return redirect('/admin/projects/vulnerability/')
            
    # Fetch all projects to show in the dropdown menu
    projects = Project.objects.all()
    return render(request, 'projects/upload.html', {'projects': projects})

def download_report(request, project_id):
    """
    Triggers the download of the Word report for a specific project.
    """
    file_stream = generate_assessment_report(project_id)
    
    # Set response headers for file download
    response = HttpResponse(
        file_stream.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
    response['Content-Disposition'] = f'attachment; filename=VulnSync_Report_{project_id}.docx'
    
    return response