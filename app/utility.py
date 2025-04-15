

def find_max_rank():
    from .models import Project
    ranks = Project.objects.values_list('rank', flat=True)
    if ranks:
        return max(ranks) + 1
    else:
        return 1