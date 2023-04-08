Django CBV

📌CBV 란?

클래스형 뷰의 약자로 Class로 Views.py를 구성하는 것
다른 말로 제네릭뷰(generic view)라고도 함
장고에서 자주 쓰는 기능들을 클래스로 미리 구현해둔 것

📌CBV VS FBV

Django에서 뷰(View)를 구현하는 방법에는 Function-based views(FBV)와 Class-based views(CBV)

1. 코드의 양
   CBV는 상속을 이용하여 뷰를 구현하므로, FBV에 비해 코드의 양이 적음
   또한, CBV는 코드의 재사용성이 높으므로, 비슷한 기능을 하는 뷰를 구현할 때 코드의 중복을 피할 수 있음

2.유연성
FBV는 함수를 이용하여 뷰를 구현하므로, 뷰의 로직을 자유롭게 구현할 수 있음
따라서, 복잡한 로직을 구현해야 하는 경우에는 FBV를 사용
CBV는 상속을 이용하여 뷰를 구현하므로, 클래스의 구조에 따라 뷰의 로직을 구현
따라서, 비교적 간단한 로직을 구현해야 하는 경우에는 CBV를 사용

3.URLconf와의 연동
FBV는 URLconf와 직접적으로 연동 즉, URLconf에서 뷰의 함수명을 직접 호출
따라서, URLconf와 뷰의 연결이 명확하게 되어 있어, 유지보수가 쉬움.
CBV는 URLconf와 간접적으로 연동 즉, URLconf에서는 뷰 클래스를 호출하며, 뷰 클래스 내부에서 적절한 메서드가 호출
따라서, URLconf와 뷰 클래스의 연결이 명확하지 않을 수 있으며, 유지보수가 어려울 수 있음.

4.기능
CBV는 다양한 기능을 제공합니다. 예를 들어, CRUD(Create, Retrieve, Update, Delete) 기능을 구현할 때에는 CBV를 이용하면 간단하게 구현 가능
또한, mixin을 이용하여 뷰의 기능을 확장 가능
FBV는 기본적인 뷰 기능만 제공하므로, 뷰의 기능을 구현할 때에는 직접 구현

📌CBV 장점

1. GET, POST 등 HTTP 메소드에 따른 처리 코드 작성 시, if 함수 대신 메소드 명
   -> 코드 구조 깔끔
2. 상속과 오버라이딩 사용 가능
   -> 중복되는 코드 최소화
   -> 가독성, 효율 UP

📌CBV 사용 가이드라인

1. 뷰는 간단 명료해야함
2. 뷰 코드의 양은 적을수록 좋음
3. 뷰 안에서 같은 코드를 반복적으로 사용되지 X
4. 뷰는 프레젠테이션 로직에서 관리, 비즈니스 로직은 모델에서 처리 (특별한 경우에만 폼에서 처리)
   - 프레젠테이션 로직 : 사용자에게 보여줄 데이터를 적절히 가공, 템플릿으로 전달해 화면에 렌더링
   - 비즈니스 로직 : 데이터의 생성, 수정, 삭제 와 같은 작업 -> 데이터베이스와 밀접한 관련
5. 403, 404, 500 에러 핸들링은 CBV 이용하지 않고 FBV를 이용
6. 믹스인 간단명료해야 함

📌제너릭 뷰와 상속

1. 기반 뷰 (Base View)
   : 뷰 클래스 생성, 다른 제너릭뷰의 부모 클래스가 되는 기본 제너릭뷰
2. 제너릭 보기 뷰 (Generic Display View)
   : 객체의 목록 또는 하나의 객체 상세 정보 보여주는 뷰
3. 제너릭 수정 뷰 (Generic Edit View)
   : 폼을 통해 객체 생성, 수정, 삭제하는 기능을 제공하는 뷰
4. 제너릭 날짜 뷰 (Generic Date View)
   : 날짜 기반 객체의 연/월/일 페이지로 구분해 보여주는 뷰

📌주요 제너릭 뷰 목록

1. 기반 뷰(Base View)

   - View : 최상위 부모 제너릭 뷰 클래스
   - TemplateView : 주어진 템플릿으로 렌더링
   - RedirectView : 주어진 URL로 리다이렉트

2. 제너릭 보기 뷰(Generic Display View)

   - DetailView : 조건에 맞는 하나의 객체 출력
   - ListView : 조건에 맞는 객체 목록 출력

3. 제너릭 수정 뷰(Generic Edit View)
   - FormView : 폼이 주어지면 해당 폼을 출력
   - CreateView : 객체를 생성하는 폼 출력
   - UpdateView : 기존 객체를 수정하는 폼을 출력
   - DeleteView : 기존 객ㅊ를 삭제하는 폼을 출력

4.제너릭 날짜 뷰(Generic Date View) - YearArchiveView : 주어진 연도에 해당하는 객체 출력 - MonthArchiveView : 주어진 월에 해당하는 객체 출력 - DayArchiveView : 주어진 날짜에 해당하는 객체 출력 - TodayArchiveView : 오늘 날짜에 해당하는 객체 출력 - DateDetailView : 주어진 연,월,일 PK(또는 슬러그)에 해당하는 객체 출력

📌제너릭 뷰 오버라이딩

1. 속성 변수 오버라이딩
   - model : 기본뷰(View, Template, RedirectView) 3개를 제외하고
     모든 제너릭뷰에서 사용
   - queryset : 기본뷰(View, Template, RedirectView) 3개를 제외하고
     모든 제너릭뷰에서 사용
     queryset 사용하면 model 속성은 무시됨
   - template_name : TemplateView를 포함한 모든 제너릭 뷰에서 사용
     템플릿 파일명을 문자열로 지정
   - context_object_name : 뷰에서 템플릿 파일에 전달하는 컨텍스트 변수명 지정
   - paginate_by : ListView와 날짜 기반뷰에서 사용
     페이징 기능이 활성화 된 경우 페이지 당 출력 항목 수를 정수로 지정
   - date_Field : 날짜 기반 뷰에서 사용
     필드의 타입은 DateField or DateTimeField
   - form_class : FormView, CreateView, UpdateView에서 폼을 만드는 데 사용할
     클래스 지정
   - success_url : FormView, CreateView, UpdateView, DeleteView에서
     폼에 대한 처리가 성공한 후 리다이렉트할 URL 주소

📌메소드 오버라이딩

    1. def get_queryset()
    : 기본 뷰(View, TemplateView, RedirectView)를 제외하고
      모든 제너릭 뷰에서사용
      디폴트는 queryset 속성 반환
      queryset 속성이 지정되지 않은 경우
      모델 매니저 클래스의 all() 메소드 호출
        -> QuerySet 객체 생성 후 반환
    2. def get_context_data(**kwargs)
    : 뷰에서 템플릿 파일에 넘겨주는 컨텍스트 데이터를 추가하거나 변경하는 목적으로
      오버라이딩
    3. def form_valid(form)
    : 유효성 검사 -> form이 유효한 경우 호출, form이 제출될 때 호출
      form_valid() 메서드에서는 반드시 HttpResponseRedirect 객체나 HttpResponse 객체를 반환
      -> CBV에서 다음으로 이동할 URL을 결정하는 데 사용

📌 모델을 지정하는 방법 3가지

1. model 속성 변수 지정
2. querySet 속성 변수 지정
3. def get_queryset() 메소드 오버라이딩

referenced from https://wikidocs.net/9623
