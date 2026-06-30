from abc import ABC, abstractmethod


class BaseLesson(ABC):
    platform_name = "Rikkei Academy LMS"
    base_completion_points = 10

    def __init__(self, lesson_code, lesson_title):
        self.lesson_code = lesson_code
        self.lesson_title = lesson_title
        self.__duration_minutes = 0

    @property
    def duration_minutes(self):
        return self.__duration_minutes

    def _add_duration(self, minutes):
        if minutes <= 0:
            raise ValueError(
                "Duration must be greater than 0."
            )
        self.__duration_minutes += minutes

    @property
    def lesson_title(self):
        return self.__lesson_title

    @lesson_title.setter
    def lesson_title(self, value):
        self.__lesson_title = " ".join(
            value.strip().upper().split()
        )

    @abstractmethod
    def calculate_completion_score(self):
        pass

    @abstractmethod
    def update_content(self, new_data):
        pass

    def __add__(self, other):
        if not isinstance(other, BaseLesson):
            return NotImplemented
        return self.duration_minutes + other.duration_minutes

    def __lt__(self, other):
        if not isinstance(other, BaseLesson):
            return NotImplemented
        return self.duration_minutes < other.duration_minutes

    @staticmethod
    def validate_lesson_code(lesson_code):
        return (
            len(lesson_code) == 10
            and lesson_code.startswith("LMS")
        )

    @classmethod
    def update_base_points(cls, new_points):
        if new_points <= 0:
            raise ValueError(
                "Base points must be greater than 0."
            )
        cls.base_completion_points = new_points


class VideoLesson(BaseLesson):
    def __init__(
        self,
        lesson_code,
        lesson_title,
        video_quality="1080p",
        view_count=0
    ):
        super().__init__(lesson_code, lesson_title)
        self.video_quality = video_quality
        self.view_count = view_count

    def play_video(self):
        self.view_count += 1

    def calculate_completion_score(self):
        return (
            self.base_completion_points
            + self.duration_minutes * 0.5
        )

    def update_content(self, new_data):
        if isinstance(new_data, str):
            self.video_quality = new_data
        elif isinstance(new_data, (int, float)):
            if new_data <= 0:
                raise ValueError(
                    "Duration must be greater than 0."
                )
            self._add_duration(new_data)

    def display_info(self):
        print("Lesson Type: VideoLesson")
        print("Platform:", self.platform_name)
        print("Lesson Code:", self.lesson_code)
        print("Lesson Title:", self.lesson_title)
        print("Duration:", self.duration_minutes)
        print("Video Quality:", self.video_quality)
        print("Views:", self.view_count)


class CodingChallenge(BaseLesson):
    def __init__(
        self,
        lesson_code,
        lesson_title,
        number_of_testcases=1,
        difficulty_multiplier=1.5
    ):
        super().__init__(lesson_code, lesson_title)
        self.number_of_testcases = number_of_testcases
        self.difficulty_multiplier = difficulty_multiplier

    def calculate_completion_score(self):
        return (
            self.base_completion_points
            * self.number_of_testcases
            * self.difficulty_multiplier
        )

    def update_content(self, new_data):
        if new_data <= 0:
            raise ValueError(
                "Testcases must be greater than 0."
            )

        self.number_of_testcases = new_data

    def display_info(self):
        print("Lesson Type: CodingChallenge")
        print("Platform:", self.platform_name)
        print("Lesson Code:", self.lesson_code)
        print("Lesson Title:", self.lesson_title)
        print("Duration:", self.duration_minutes)
        print("Testcases:", self.number_of_testcases)
        print("Difficulty:", self.difficulty_multiplier)


class HybridAssessment(VideoLesson, CodingChallenge):
    def __init__(
        self,
        lesson_code,
        lesson_title,
        video_quality="1080p",
        view_count=0,
        number_of_testcases=1,
        difficulty_multiplier=1.5
    ):
        VideoLesson.__init__(
            self,
            lesson_code,
            lesson_title,
            video_quality,
            view_count
        )

        self.number_of_testcases = number_of_testcases
        self.difficulty_multiplier = difficulty_multiplier

    def calculate_completion_score(self):
        video_score = (
            self.base_completion_points
            + self.duration_minutes * 0.5
        )

        coding_score = (
            self.base_completion_points
            * self.number_of_testcases
            * self.difficulty_multiplier
        )

        return video_score + coding_score

    def update_content(self, new_data):
        if new_data <= 0:
            raise ValueError(
                "Data must be greater than 0."
            )

        self.number_of_testcases = new_data

    def display_info(self):
        print("Lesson Type: HybridAssessment")
        print("Platform:", self.platform_name)
        print("Lesson Code:", self.lesson_code)
        print("Lesson Title:", self.lesson_title)
        print("Duration:", self.duration_minutes)
        print("Video Quality:", self.video_quality)
        print("Views:", self.view_count)
        print("Testcases:", self.number_of_testcases)
        print("Difficulty:", self.difficulty_multiplier)

    def show_mro(self):
        for cls in HybridAssessment.__mro__:
            print(cls.__name__)


class AWSS3StorageService:
    def upload_lesson(self, lesson):
        print("[AWS S3]: Connecting...")
        print("Duck Typing authentication successful!")
        print(
            "Lesson",
            lesson.lesson_code,
            "uploaded successfully."
        )


class GoogleCloudStorageService:
    def upload_lesson(self, lesson):
        print("[Google Cloud]: Connecting...")
        print("Duck Typing authentication successful!")
        print(
            "Lesson",
            lesson.lesson_code,
            "uploaded successfully."
        )


def sync_to_cloud(cloud_service, lesson):
    try:
        cloud_service.upload_lesson(lesson)
    except AttributeError:
        print(
            "Invalid cloud service."
        )


lessons = []
current_lesson = None


def create_lesson():
    global current_lesson

    print("\n--- CHOOSE LESSON TYPE ---")
    print("1. Video Lesson")
    print("2. Coding Challenge")
    print("3. Hybrid Assessment")

    try:
        choice = int(input("Choose type (1-3): "))
    except ValueError:
        print("Invalid choice.")
        return

    lesson_code = input("Enter lesson code: ").strip()

    if not BaseLesson.validate_lesson_code(lesson_code):
        print("Invalid lesson code.")
        return

    lesson_title = input("Enter lesson title: ")

    if choice == 1:
        lesson = VideoLesson(lesson_code, lesson_title)

    elif choice == 2:
        lesson = CodingChallenge(lesson_code, lesson_title)

    elif choice == 3:
        lesson = HybridAssessment(lesson_code, lesson_title)

    else:
        print("Lesson type does not exist.")
        return

    lessons.append(lesson)
    current_lesson = lesson

    print("Lesson created successfully!")
    print("Lesson Title:", current_lesson.lesson_title)


def show_current_lesson():
    if current_lesson is None:
        print("No lesson selected.")
        return

    print("\n--- LESSON INFORMATION ---")
    current_lesson.display_info()

    print("\n--- MRO ---")
    for cls in type(current_lesson).__mro__:
        print(cls.__name__)


def choose_lesson():
    if len(lessons) == 0:
        print("Lesson list is empty.")
        return None

    print("\nLesson List")

    for i in range(len(lessons)):
        print(
            i + 1,
            lessons[i].lesson_code,
            lessons[i].lesson_title
        )

    try:
        index = int(input("Choose lesson: ")) - 1

        if index < 0 or index >= len(lessons):
            print("Invalid choice.")
            return None

        return lessons[index]

    except ValueError:
        print("Invalid input.")
        return None


def update_lesson():
    if current_lesson is None:
        print("No lesson selected.")
        return

    print("\n--- UPDATE LESSON ---")
    print("1. Play video")
    print("2. Update lesson data")

    try:
        choice = int(input("Choose: "))
    except ValueError:
        print("Invalid input.")
        return

    if choice == 1:
        if isinstance(current_lesson, (VideoLesson, HybridAssessment)):
            current_lesson.play_video()
            print("Video played successfully.")
            print("Views:", current_lesson.view_count)
        else:
            print("This lesson has no video.")

    elif choice == 2:
        if isinstance(current_lesson, (CodingChallenge, HybridAssessment)):
            try:
                testcase = int(input("Enter new number of testcases: "))
                current_lesson.update_content(testcase)
                print("Updated successfully.")
                print("Testcases:", current_lesson.number_of_testcases)
            except ValueError as e:
                print(e)

        elif isinstance(current_lesson, VideoLesson):
            print("1. Update duration")
            print("2. Update video quality")

            try:
                option = int(input("Choose: "))
            except ValueError:
                print("Invalid input.")
                return

            if option == 1:
                try:
                    duration = int(input("Enter duration: "))
                    current_lesson.update_content(duration)
                    print("Duration:", current_lesson.duration_minutes)
                except ValueError as e:
                    print(e)

            elif option == 2:
                quality = input("Enter quality: ")
                current_lesson.update_content(quality)
                print("Quality:", current_lesson.video_quality)

    else:
        print("Invalid choice.")


def completion_score():
    if current_lesson is None:
        print("No lesson selected.")
        return

    score = current_lesson.calculate_completion_score()

    print("\n--- COMPLETION SCORE ---")
    print("Lesson:", current_lesson.lesson_title)
    print("Type:", type(current_lesson).__name__)
    print(
        "Base Points:",
        BaseLesson.base_completion_points
    )
    print(
        "Duration:",
        current_lesson.duration_minutes
    )

    if isinstance(current_lesson, (CodingChallenge, HybridAssessment)):
        print(
            "Testcases:",
            current_lesson.number_of_testcases
        )

    print("Score:", score)


def compare_lessons():
    if current_lesson is None:
        print("No lesson selected.")
        return

    if len(lessons) < 2:
        print("Need at least two lessons.")
        return

    other = choose_lesson()

    if other is None:
        return

    if other == current_lesson:
        print("Cannot compare with itself.")
        return

    try:
        if current_lesson < other:
            print("Current lesson is shorter.")
        else:
            print("Current lesson is longer or equal.")

        total = current_lesson + other
        print("Total Duration:", total, "minutes")

    except TypeError:
        print("Comparison failed.")


def cloud_sync():
    if current_lesson is None:
        print("No lesson selected.")
        return

    print("\n1. AWS S3")
    print("2. Google Cloud")

    try:
        choice = int(input("Choose service: "))
    except ValueError:
        print("Invalid input.")
        return

    if choice == 1:
        service = AWSS3StorageService()

    elif choice == 2:
        service = GoogleCloudStorageService()

    else:
        print("Invalid choice.")
        return

    sync_to_cloud(service, current_lesson)


def show_menu():
    print("\n========== LMS MENU ==========")
    print("1. Create Lesson")
    print("2. View Lesson")
    print("3. Update Lesson")
    print("4. Completion Score")
    print("5. Operator Overloading")
    print("6. Cloud Sync")
    print("7. Exit")
    print("==============================")


while True:
    show_menu()

    try:
        choice = int(input("Choose: "))
    except ValueError:
        print("Invalid input.")
        continue

    if choice == 1:
        create_lesson()

    elif choice == 2:
        show_current_lesson()

    elif choice == 3:
        update_lesson()

    elif choice == 4:
        completion_score()

    elif choice == 5:
        compare_lessons()

    elif choice == 6:
        cloud_sync()

    elif choice == 7:
        print("Thank you for using the system.")
        break

    else:
        print("Invalid choice.")
