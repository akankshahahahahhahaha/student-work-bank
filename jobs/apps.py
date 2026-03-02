from django.apps import AppConfig

class JobsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jobs'

    def ready(self):
        from jobs.models import Job

        if Job.objects.count() == 0:
            Job.objects.create(
                title="Frontend Developer Intern",
                company="TechNova Solutions",
                location="Pune, India",
                description="Work on responsive UI using React and Tailwind CSS."
            )

            Job.objects.create(
                title="Backend Developer Intern",
                company="CodeSphere Labs",
                location="Remote",
                description="Build REST APIs using Django and PostgreSQL."
            )

            Job.objects.create(
                title="AI/ML Intern",
                company="DataMind Analytics",
                location="Bangalore, India",
                description="Work on ML models and NLP projects."
            )

            Job.objects.create(
                title="Social Media Manager Intern",
                company="BrandBoost Media",
                location="Mumbai, India",
                description="Handle reels strategy and brand campaigns."
            )

            print("Sample jobs inserted.")