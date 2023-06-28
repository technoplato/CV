export interface Location {
  address: string;
  postalCode: string;
  city: string;
  countryCode: string;
  region: string;
}

export interface Profile {
  network: string;
  username: string;
  url: string;
}

export interface BasicInfo {
  name: string;
  label: string;
  image: string;
  email: string;
  phone: string;
  url: string;
  summary: string;
  location: Location;
  profiles: Profile[];
}

export interface WorkExperience {
  name: string;
  position: string;
  url?: string;
  startDate: string;
  endDate: string;
  summary: string;
  highlights: string[];
  technologies: string[];
}

export interface Project {
  name: string;
  type: string;
  role: string;
  technologies: string[];
  description: string;
  github?: string;
  client?: string;
  features?: string[];
  appStore?: string;
  demo?: string;
  responsibilities?: string[];
  year?: number;
  link?: string;
}

export interface Education {
  institution: string;
  area: string;
  studyType: string;
  startDate: string;
  endDate: string;
  gpa: string;
  courses: string[];
}

export interface Award {
  title: string;
  date: string;
  awarder: string;
  summary: string;
}

export interface Publication {
  name: string;
  publisher: string;
  releaseDate: string;
  url: string;
}

export interface Skill {
  name: string;
  level: string;
  keywords: string[];
}

export interface Language {
  language: string;
  fluency: string;
}

export interface Interest {
  name: string;
  keywords: string[];
}

export interface Resume {
  basics: BasicInfo;
  work: WorkExperience[];
  projects: Project[];
  education: Education[];
  awards: Award[];
  publications: Publication[];
  skills: Skill[];
  languages: Language[];
  interests: Interest[];
  references: any[];
  volunteer: any[];
}
