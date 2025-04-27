[Project homepage](https://github.com/peter88213/novx_html) > User guide

---

# novx_html User guide

The novx_html Python script runs through all chapters and sections of a novelibre project and fills HTML templates.

## Usage

usage: `novx_html.py [-h] [-t template-dir] [-s suffix] [--silent] Project`

#### positional arguments:

 `Project`     novelibre project file

#### optional arguments:

 `-h, --help`    show a help message and exit
 
 `-t template-dir` template directory
 
 `-s suffix`    suffix to output file name
 
 `--silent`     suppress error messages and the request to confirm overwriting

If no template directory is set, templates are searched for in the novelibre 
project directory.

If no templates are found, the output file will be empty.


## Examples

The downloaded zip file includes a directory named `sample` containing example templates 
for different purposes and some example batch files showing the correct commands. 
You can launch the batch files by dragging and dropping your novelibre project on 
the icons. 
The results will be written to the novelibre project directory.


## Templates

### Project level templates

- `html_header.html`

- `character_template.html`(applied to characters)
- `location_template.html`(applied to locations)
- `item_template.html`(applied to items)

- `html_footer.html`

### Chapter level templates

- `part_template.html`(part header; applied to all "normal" parts)
- `chapter_template.html`(chapter header; applied to all "normal" chapters)
- `unused_chapter_template.html`(chapter header; applied to all "unused" chapters)


- `chapter_end_template.html`(chapter footer; applied to all "normal" chapters)
- `unused_chapter_end_template.html`(chapter footer; applied to all "unused" chapters)



### Section level templates

- `section_template.html`(applied to "normal" sections within "normal" chapters)
- `appended_section_template.html`(optional; applied to "normal" sections that are appended to the previous one)
- `first_section_template.txt`(optional; applied  to "normal" sections at the beginning of the chapter)
- `unused_section_template.html`(applied to "unused" sections)
- `section_divider.html`(lead sections, beginning from the second in chapter)


## Placeholders

### Syntax

There are two options:

1.  `$Placeholder` - If the placeholder is followed by a character that
    is clearly recognizable as a separator, e.g. a blank.
2.  `${Placeholder}` - If the placeholder is followed by a character
    that is not recognizable as a separator.

### "Project template" placeholders

-   `$Title` - Project title
-   `$Desc` - Project description consisting of ready-formatted paragraphs
-   `$AuthorName` - Author\'s name
-   `$Language` - Language code acc. to ISO 639-1
-   `$Country` - Country code acc. to ISO 3166-2
-   `$CustomPlotProgress` - Custom "Plot progress" field title
-   `$CustomCharacterization` - Custom "Characterization" field title
-   `$CustomWorldBuilding` - Custom "World building" field title
-   `$CustomGoal` - Custom "Goal" field title
-   `$CustomConflict` - Custom "Conflict" field title
-   `$CustomOutcome` - Custom "Outcome" field title
-   `$CustomChrBio` - Custom character "Bio" field title
-   `$CustomChrGoals` - Custom character "Goals" field title

## "Chapter template" placeholders

-   `$ID` - Chapter ID,
-   `$ChapterNumber` - Chapter number (in sort order),
-   `$Title` - Chapter title
-   `$Desc` - Chapter description consisting of ready-formatted paragraphs
-   `$Epigraph` - Epigraph consisting of ready-formatted paragraphs
-   `$EpigraphSrc` - Epigraph source
-   `$Notes` - Chapter notes consisting of ready-formatted paragraphs
-   `$ProjectName` - URL-coded file name without suffix and extension
-   `$ProjectPath` - URL-coded fpath to the project directory
-   `$Language` - Language code acc. to ISO 639-1
-   `$Country` - Country code acc. to ISO 3166-2
-   `$ManuscriptSuffix` - File name suffix of the manuscript

## "Section template" placeholders

-   `$ID` - Section ID,
-   `$SectionNumber` - Section number (in sort order),
-   `$Title` - Section title
-   `$Desc` - Section description consisting of ready-formatted paragraphs
-   `$WordCount` - Section word count
-   `$WordsTotal` - Accumulated word count including the current section
-   `$Status` - Section status (Outline, Draft etc.)
-   `$SectionContent` - Section content consisting of ready-formatted paragraphs
-   `$Date` - Specific section date (YYYY-MM-DD)
-   `$Time` - Time section begins: (hh:mm)
-   `$OdsTime` - Time section begins: (PThhHmmMssS)
-   `$Day` - Day section begins
-   `$ScDate` - Date or day (localized)
-   `$DateYear` - Year
-   `$DateMonth` - Month (number)
-   `$DateDay` - Day (number)
-   `$DateWeekday` - Day of the week (name)
-   `$MonthName` - Month (name)
-   `$LastsDays` - Amount of time section lasts: days
-   `$LastsHours` - Amount of time section lasts: hours
-   `$LastsMinutes` - Amount of time section lasts: minutes
-   `Duration` - Combination of days and hours and minutes
-   `$Scene` - The sections\'s kind of scene, if any
-   `$Goal` - The section protagonist\'s goal consisting of ready-formatted paragraphs
-   `$Conflict` - The section conflict consisting of ready-formatted paragraphs
-   `$Outcome` - The section outcome consisting of ready-formatted paragraphs
-   `$Tags` - Comma-separated list of section tags
-   `$Characters` - Comma-separated list of characters assigned to the
    section
-   `$Viewpoint` - Viewpoint character
-   `$Locations` - Comma-separated list of locations assigned to the
    section
-   `$Items` - Comma-separated list of items assigned to the section
-   `$Notes` - Section notes consisting of ready-formatted paragraphs
-   `$ProjectName` - URL-coded file name without suffix and extension
-   `$ProjectPath` - URL-coded fpath to the project directory
-   `$Language` - Language code acc. to ISO 639-1
-   `$Country` - Country code acc. to ISO 3166-2
-   `$ManuscriptSuffix` - File name suffix of the manuscript
-   `$SectionsSuffix` - File name suffix of the section descriptions
-   `$CustomPlotProgress` - Custom "Plot progress" field title
-   `$CustomCharacterization` - Custom "Characterization" field title
-   `$CustomWorldBuilding` - Custom "World building" field title
-   `$CustomGoal` - Custom "Goal" field title
-   `$CustomConflict` - Custom "Conflict" field title
-   `$CustomOutcome` - Custom "Outcome" field title
